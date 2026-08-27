"""Rebuild the 绥化高考 dataset and interactive page from the markdown source.

    python3 scripts/build-suihua.py

Reads   content/2007/suihua.md          (the source of truth — edit this)
Writes  content/2007/suihua.csv         (flat table, one row per 上榜考生)
        static/suihua/index.html        (self-contained interactive page)

The markdown is parsed by structure, not by line number: a `## <year>年` heading
opens a year, a heading containing 理 or 文 opens a track, and every following
6-column table row is a record. Add years, rows, scores or 备注 text and rerun.

    --check   parse and report only; write nothing
"""

import argparse
import csv
import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "content" / "2007" / "suihua.md"
CSV_OUT = ROOT / "content" / "2007" / "suihua.csv"
TEMPLATE = ROOT / "scripts" / "suihua-template.html"
HTML_OUT = ROOT / "static" / "suihua" / "index.html"

CSV_HEADER = ["年份", "文理科", "全市名次", "姓名", "毕业中学", "分数", "录取院校", "备注"]

# 绥化 / 安达 / 肇东 / 海伦 were all 撤县设市; "X县Y中学" and "X市Y中学" are one school.
# Everywhere else 县 is still a county and is left alone.
UPGRADED_COUNTIES = ("绥化", "安达", "肇东", "海伦")

# Historic names, campuses and 专项 batches that are one institution today.
UNI_ALIAS = {
    "清华大学（专项）": "清华大学",
    "北京大学（专项）": "北京大学",
    "北京大学医学部": "北京大学", "北京大学（医学部）": "北京大学",
    "北京大学医学院": "北京大学", "北京医科大学": "北京大学",
    "中国人民大学（专项）": "中国人民大学", "中国人民大学（苏州）": "中国人民大学",
    "复旦大学医学院": "复旦大学", "上海复旦大学": "复旦大学",
    "上海交通大学医学院": "上海交通大学",
    "中国科技大学": "中国科学技术大学",
    "中国科技大学（首届少年班）": "中国科学技术大学",
    "北京航空学院": "北京航空航天大学", "北京航天航空学院": "北京航空航天大学",
    "北京航空航天学院": "北京航空航天大学",
    "北京工业学院": "北京理工大学",
    "北京政法学院": "中国政法大学",
    "大连工学院": "大连理工大学",
    "北方交通大学": "北京交通大学",
    "哈尔滨建工学院": "哈尔滨工业大学",
    "白求恩医科大学": "吉林大学",
    "吉林师范大学": "东北师范大学",
    "哈尔滨师范学院": "哈尔滨师范大学",
    "东北重型机械学院": "燕山大学",
    "大庆石油学院": "东北石油大学",
    "辽宁财经学院": "东北财经大学",
    "南京航空学院": "南京航空航天大学",
    "北京商学院": "北京工商大学",
    "北京外国语学院": "北京外国语大学",
    "北京物资学院": "北京物资大学",
    "西北政法学院": "西北政法大学",
    "长春税务学院": "吉林财经大学",
    "齐齐哈尔师范学院": "齐齐哈尔大学",
    "中国计量学院": "中国计量大学",
    "中国国际关系学院": "国际关系学院",
    "中国人民警官大学": "中国人民公安大学",
    "解放军第四军医大学": "空军军医大学",
    "南京铁道学院": "东南大学",
}

# 单校录取院校明细 lists only these 13: the C9 League plus 人大 / 北师大 / 北航 / 同济.
DETAIL_UNIS = [
    "清华大学", "北京大学", "复旦大学", "上海交通大学", "浙江大学", "南京大学",
    "中国科学技术大学", "哈尔滨工业大学", "西安交通大学",
    "中国人民大学", "北京师范大学", "北京航空航天大学", "同济大学",
]

# 绥化市第一中学 principals, by actual appointment date ("YYYY" or "YYYY.M").
# `hue` picks the band colour (--era-bg-* / --era-ink-* in the template); the
# order green→violet→amber→blue→red keeps neighbouring eras easy to tell apart.
#
# A band is placed on the exam years the principal was actually in post FOR —
# the gaokao sits in June/July, so a handover in, say, 2005.2 gives that year's
# exam to the incoming principal while one in 2014.8 leaves it with the outgoing
# one. Years no listed principal covers simply get no band.
ERAS = [
    {"name": "盛向君", "from": "1980",   "to": "1999.11", "hue": 1},
    {"name": "宋官雅", "from": "1999.11", "to": "2001.3", "hue": 2},
    {"name": "张玉臣", "from": "2001.3",  "to": "2005.2", "hue": 3},
    {"name": "魏志波", "from": "2005.2",  "to": "2014.8", "hue": 4},
    {"name": "白云霞", "from": "2014.8",  "to": "2020.10", "hue": 5},
]
ERA_SCHOOL = "绥化市第一中学"


def exam_month(year):
    """When that year's 高考 was held: Dec in 1977, July until 2002, June since 2003."""
    if year == 1977:
        return 12
    return 7 if year < 2003 else 6


def parse_when(text):
    """'1999.11' -> (1999, 11); '1980' -> (1980, 1)."""
    parts = str(text).split(".")
    return (int(parts[0]), int(parts[1]) if len(parts) > 1 else 1)


def build_eras(ymin, ymax):
    """Map each tenure onto the exam years it actually covers."""
    out = []
    for e in ERAS:
        start, end = parse_when(e["from"]), parse_when(e["to"])
        if start >= end:
            raise SystemExit(f"ERAS: {e['name']} starts at or after it ends")
        years = [y for y in range(ymin, ymax + 1)
                 if start <= (y, exam_month(y)) < end]
        if not years:
            continue                      # tenure falls outside the data's years
        out.append({"name": e["name"], "hue": e["hue"],
                    "label": f"{e['from']}–{e['to']}",
                    "start": years[0], "end": years[-1]})
    return out

QINGBEI = {"清华大学", "北京大学"}
C9_OTHER = {"复旦大学", "上海交通大学", "浙江大学", "南京大学",
            "中国科学技术大学", "哈尔滨工业大学", "西安交通大学"}
ELITE = {
    "中国人民大学", "南开大学", "北京师范大学", "北京航空航天大学", "同济大学",
    "天津大学", "武汉大学", "中山大学", "厦门大学", "山东大学", "吉林大学",
    "中南大学", "四川大学", "华东师范大学", "大连理工大学", "湖南大学",
    "中国农业大学", "北京理工大学", "西北大学", "国防科技大学", "空军军医大学",
    "中央美术学院", "东南大学",
}
TIERS = ["清华 / 北大", "其余 C9", "其他 985 / 顶尖", "其他院校", "院校未记录"]
NO_UNI_TIER = 4   # ranked student whose 录取院校 is blank in the source

# A year heading is "## 1983年", "## 1983", or "### 1988 年普通高校招生…" —
# 年 is optional so a heading that omits it cannot silently fold one year
# into the previous one.
YEAR_RE = re.compile(r"^#+\s*(\d{4})\s*(?:年.*)?$")
SEP_RE = re.compile(r"^\|[\s\-:|]+\|$")
SCORE_RE = re.compile(r"(\d+(?:\.\d+)?)")
RANK_RE = re.compile(r"^\d+$")


def normalize_school(name):
    for city in UPGRADED_COUNTIES:
        name = name.replace(city + "县", city + "市")
    return name


def merge_county_city(records):
    """A name differing from another only by 县/市 is the same school.

    绥化/安达/肇东/海伦 are already normalised to 市 above; this catches the rest
    (and any stray typo) by folding each 县/市 pair onto whichever spelling the
    source uses more often. Returns the list of merges applied.
    """
    counts = Counter(r["毕业中学"] for r in records)
    groups = {}
    for name, n in counts.items():
        groups.setdefault(name.replace("县", "市"), []).append((n, name))

    remap, merges = {}, []
    for variants in groups.values():
        if len(variants) < 2:
            continue
        variants.sort(reverse=True)          # most frequent spelling wins
        winner = variants[0][1]
        for n, loser in variants[1:]:
            remap[loser] = winner
            merges.append((loser, n, winner, variants[0][0]))

    if remap:
        for r in records:
            r["毕业中学"] = remap.get(r["毕业中学"], r["毕业中学"])
    return merges


def tier_of(uni):
    if uni in QINGBEI:
        return 0
    if uni in C9_OTHER:
        return 1
    if uni in ELITE:
        return 2
    return 3


def parse(md_path):
    """Return (records, skipped_lines). Each record is a dict of CSV_HEADER fields."""
    records, skipped = [], []
    year = track = None

    for lineno, raw in enumerate(md_path.read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip()
        if not line:
            continue

        if line.startswith("#"):
            text = line.lstrip("#").strip()
            matched_year = YEAR_RE.match(line)
            if matched_year:
                year = matched_year.group(1)
            # a heading may carry both, e.g. "### 1988 年…理科类前十名…"
            if "理" in text:
                track = "理科"
            elif "文" in text:
                track = "文科"
            elif matched_year:
                track = None
            continue

        if not line.startswith("|"):
            skipped.append((lineno, "prose", line))
            continue
        if SEP_RE.match(line):
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0] in ("名次", "排名", "全市名次"):
            continue
        if len(cells) != 6:
            skipped.append((lineno, f"{len(cells)} columns, expected 6", line))
            continue
        if year is None or track is None:
            skipped.append((lineno, "no enclosing 年份/科类 heading", line))
            continue

        rank, name, school, score, uni, note = cells
        records.append({
            "年份": year, "文理科": track, "全市名次": rank, "姓名": name,
            "毕业中学": normalize_school(school), "分数": score,
            "录取院校": uni, "备注": note,
        })

    return records, skipped


def write_csv(records, path):
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(CSV_HEADER)
        writer.writerows([[r[k] for k in CSV_HEADER] for r in records])


def ranked(records):
    """Only rows carrying an actual rank number count as 前十."""
    return [r for r in records if RANK_RE.match(r["全市名次"].strip())]


def build_payload(records):
    # 姓名 is carried ONLY where the page actually prints it: 清华/北大 admits and
    # rows carrying a 备注, both listed by name in 单校录取院校明细. Every other
    # student's name stops at the CSV — the page ships to the web, so the exposure
    # is held to exactly the displayed set.
    #
    # Every student is carried, ranked or not, with rank 0 meaning "no rank number
    # in the source". The page counts 前十人数 over rank > 0 only, but counts
    # admissions (清北, the 13 schools) over everyone.
    rows = []
    for r in records:
        uni = UNI_ALIAS.get(r["录取院校"], r["录取院校"]).strip()
        found = SCORE_RE.search(r["分数"]) if r["分数"] not in ("无", "") else None
        rank = r["全市名次"].strip()
        rows.append({
            "y": int(r["年份"]),
            "t": 0 if r["文理科"] == "理科" else 1,
            "rank": int(rank) if RANK_RE.match(rank) else 0,
            "school": r["毕业中学"],
            "uni": uni, "raw": r["录取院校"], "note": r["备注"],
            "score": float(found.group(1)) if found else None,
            "tier": tier_of(uni) if uni else NO_UNI_TIER,
            "name": r["姓名"],
        })
    for x in rows:
        if x["tier"] != 0 and not x["note"]:
            x["name"] = ""            # drop every undisplayed name before it reaches the page

    schools = [s for s, _ in Counter(x["school"] for x in rows).most_common()]
    unis = [u for u, _ in Counter(x["uni"] for x in rows if x["uni"]).most_common()]
    raws = sorted({x["raw"] for x in rows if x["uni"] and x["raw"] != x["uni"]})
    si = {s: i for i, s in enumerate(schools)}
    ui = {u: i for i, u in enumerate(unis)}
    ri = {v: i for i, v in enumerate(raws)}
    ymin, ymax = min(x["y"] for x in rows), max(x["y"] for x in rows)

    eras = build_eras(ymin, ymax)
    for a, b in zip(eras, eras[1:]):
        if a["end"] >= b["start"]:
            raise SystemExit(f"ERAS overlap on exam years: {a['name']} ends "
                             f"{a['end']}, {b['name']} starts {b['start']}")

    return {
        "schools": schools, "unis": unis, "raws": raws, "tiers": TIERS,
        "ymin": ymin, "ymax": ymax,
        "detailUnis": [u for u in DETAIL_UNIS if u in ui],
        "eras": eras, "eraSchool": ERA_SCHOOL,
        # [year, track, rank, schoolIdx, uniIdx, tier, score, rawIdx, note, name]
        # name is non-empty only for tier 0 (清华/北大)
        "rows": [[x["y"], x["t"], x["rank"], si[x["school"]], ui.get(x["uni"], -1),
                  x["tier"], x["score"], ri.get(x["raw"], -1), x["note"], x["name"]]
                 for x in rows],
    }


def render_html(payload, template_path, out_path):
    template = template_path.read_text(encoding="utf-8")
    if "__DATA__" not in template:
        raise SystemExit(f"{template_path} has no __DATA__ placeholder")
    blob = json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    if "</script" in blob:
        raise SystemExit("data contains a </script sequence and would break the page")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(template.replace("__DATA__", blob), encoding="utf-8")
    return len(blob)


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="parse and report only; write nothing")
    args = ap.parse_args()

    records, skipped = parse(SRC)
    if not records:
        raise SystemExit(f"no records parsed from {SRC}")

    merges = merge_county_city(records)

    payload = build_payload(records)
    keep = ranked(records)
    dropped = [r for r in records if r not in keep]
    years = sorted({r["年份"] for r in keep})
    notes = sum(1 for r in keep if r["备注"])
    scores = sum(1 for r in keep if r["分数"] not in ("无", ""))

    print(f"{len(keep)} ranked records · {len(years)} years {years[0]}–{years[-1]} · "
          f"{len(payload['schools'])} schools · {len(payload['unis'])} universities")
    print(f"  scores present: {scores}   备注 present: {notes}")
    if dropped:
        by = Counter((r["年份"], r["文理科"]) for r in dropped)
        print(f"  {len(dropped)} row(s) without a rank number excluded from 前十: "
              + ", ".join(f"{y}{t}×{n}" for (y, t), n in sorted(by.items())))

    if merges:
        print("  merged 县/市 spellings of the same school:")
        for loser, ln, winner, wn in merges:
            print(f"      {loser} ({ln}) -> {winner} ({wn})")

    blank = [row for row in payload["rows"] if row[5] == NO_UNI_TIER]
    if blank:
        rb = sum(1 for row in blank if row[2] > 0)
        print(f"  {len(blank)} row(s) with no 录取院校 ({rb} of them ranked, "
              f"counted in 前十 but not in any 院校 total)")

    named = sum(1 for row in payload["rows"] if row[9])
    print(f"  {named} name(s) carried into the page (清北 + 备注 rows); "
          f"{len(payload['rows']) - named} other name(s) withheld")

    qb = Counter(payload["schools"][row[3]] for row in payload["rows"] if row[5] == 0)
    qb_unranked = sum(1 for row in payload["rows"] if row[5] == 0 and row[2] == 0)
    print(f"  清北 total: {sum(qb.values())}  (含 {qb_unranked} 名未列名次者)")
    for school, count in qb.most_common(5):
        print(f"      {count:4d}  {school}")

    print("  校长任期 → 高考年份:")
    covered = set()
    for e in payload["eras"]:
        span = str(e["start"]) if e["start"] == e["end"] else f"{e['start']}–{e['end']}"
        print(f"      {e['name']}  {e['label']:>16}  ->  {span}")
        covered.update(range(e["start"], e["end"] + 1))
    gaps = [y for y in range(payload["ymin"], payload["ymax"] + 1) if y not in covered]
    if gaps:
        print(f"      no listed principal: {', '.join(map(str, gaps))}")

    thin = [(y, t) for (y, t), n in
            Counter((r["年份"], r["文理科"]) for r in keep).items() if n < 10]
    if thin:
        print(f"  note: {len(thin)} year/track group(s) with fewer than 10 rows: "
              + ", ".join(f"{y}{t}" for y, t in sorted(thin)))
    broken = [s for s in skipped if s[1] != "prose"]
    prose = [s for s in skipped if s[1] == "prose" and s[2] != "---"]
    if broken:
        print(f"\n  !! {len(broken)} table row(s) DROPPED — fix these in the markdown:")
        for lineno, why, text in broken:
            print(f"      line {lineno} ({why}): {text[:76]}")
    if prose:
        print(f"  {len(prose)} prose line(s) outside tables, ignored as narrative:")
        for lineno, _, text in prose[:6]:
            print(f"      line {lineno}: {text[:70]}")
        if len(prose) > 6:
            print(f"      … and {len(prose)-6} more")

    if args.check:
        print("\n--check: nothing written")
        return

    write_csv(records, CSV_OUT)
    size = render_html(payload, TEMPLATE, HTML_OUT)
    print(f"\nwrote {CSV_OUT.relative_to(ROOT)}")
    print(f"wrote {HTML_OUT.relative_to(ROOT)}  (data {size/1024:.1f} KB)")


if __name__ == "__main__":
    main()
