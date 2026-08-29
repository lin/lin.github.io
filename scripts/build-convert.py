#!/usr/bin/env python3
"""Build the 高考等位分换算 page from the 一分一段表 CSVs.

改完 content/2007/convert/ 里的任何一个 CSV，跑一次就能把页面重新生成：

    python3 scripts/build-convert.py     # 生成
    ./scripts/build-convert.py --watch   # 盯着 CSV，一存盘就重新生成
    python3 scripts/build-convert.py --check    # 只校验数据，不写文件

Reads   content/2007/convert/<year>.csv
Writes  content/2007/convert/index.html   (与数据放在一起，可直接双击打开)
        static/gaokao-convert/index.html  (站点发布用，内容完全相同)

Every year is reduced to one dense array: for each score from 150 up to that
year's highest itemised score, the number of candidates scoring at or above it.
The year's candidate count — the denominator that turns a rank into a comparable
percentile — is the value at 150.

CSV 格式在各年之间并不统一，此处按表头名解析：
  * 累计人数 / 累积人数 两种写法都有；
  * 2009 年的列序是 分数,累积人数,本段人数，与其他年相反；
  * 2004-2009 为 CRLF 换行；
  * 2006/2009 表首有若干「虚拟上限锚点」（累计人数为 0），需要剔除。

    --check   parse and report only; write nothing
    --watch   rebuild whenever a CSV or the template changes (Ctrl-C to stop)
    --quiet   only print warnings and the two output lines
    --strict  exit 1 if any ⚠ was raised (for CI / pre-commit)
"""

import argparse
import csv
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = ROOT / "content" / "2007" / "convert"
BASELINES = SRC_DIR / "baselines.csv"   # 年份,清华分数线,上海交大分数线,浙大分数线,绥化市最高分,绥化一中最高分

# 第二梯队的参照校：2013 年起上海交大在黑龙江的线抬得极高，已经贴着清华，
# 失去了「考不上清华的下一档」这个意义，改用浙江大学。
SECOND_TIER_SWITCH = 2013
SCHOOL_TOP = SRC_DIR / "suihua.csv"     # 年份,全校排名,分数（绥化一中历届前十）
CITY_TOP = SRC_DIR / "suihuashi.csv"    # 年份,全市排名,分数,高中（绥化市历届前十）

# 校名简写，用于表格里的窄格子；完整校名保留在 title 里。
NUMBERED_SCHOOL = re.compile(r"第([一二三四五六七八九十]+)中学$")


def abbrev_school(name):
    """绥化市第一中学 -> 绥化一中；安达市高级中学 -> 安达高中；青冈县第六中学 -> 青冈六中。"""
    s = (name or "").strip()
    if not s or s == "-":
        return ""
    s = NUMBERED_SCHOOL.sub(lambda m: m.group(1) + "中", s)
    if s.endswith("高级中学"):
        s = s[:-4] + "高中"
    return re.sub(r"(市|县)(?=[一二三四五六七八九十]+中$|高中$)", "", s)
TEMPLATE = ROOT / "scripts" / "convert-template.html"
OUTPUTS = [SRC_DIR / "index.html",
           ROOT / "static" / "gaokao-convert" / "index.html"]

FLOOR = 150          # 分母口径：150 分及以上
DEFAULT_YEAR = 2007  # 打开页面时的基准年
DEFAULT_SCORE = 666

CUM_HEADERS = ("累计人数", "累积人数")
SCORE_HEADER = "分数"

# 只认四位年份的文件；convert/ 下还有别的草稿 csv。
YEAR_FILE = re.compile(r"^(19|20)\d{2}$")

# 黑龙江 2024 年起实行 3+1+2，理科变为物理类。
NEW_GAOKAO_FROM = 2024

# 当年未公布逐分的一分一段表，由官方分数段累计人数推算到逐分。
# 推算过程见 content/2007/<year>.py，其结果即 convert/<year>.csv —— 本页
# 一律以这些 csv 为准，不在此处二次判断。
MODELLED = {2004, 2005, 2006, 2007, 2008, 2009}

# 官方一分一段表未公布到 150 分的年份，分母只能估计。
# 数值与依据见页脚说明；uncertainty 是相对误差，用于界面上的可信度提示。
ESTIMATED_TOTAL = {
    2004: {"total": 108200, "from": 200, "uncertainty": 0.003,
           "basis": "该年表止于 200 分（107,116 人），150–199 分的人数按 2005/2007/2009 三年的同段占比推得"},
    2006: {"total": 134000, "from": 450, "uncertainty": 0.05,
           "basis": "该年表止于 450 分（70,980 人），分母取 2005 年 128,223 与 2007 年 139,653 之间的插值"},
    2008: {"total": 140500, "from": 300, "uncertainty": 0.02,
           "basis": "该年表止于 300 分（126,220 人），分母取 2007 年 139,653 与 2009 年 140,812 之间的插值"},
}

# 表头首行写作「710以上」「694及以上」时，该分以上未逐分公布。
OPEN_TOP = re.compile(r"以上|及以上")


def read_year(path):
    """-> (rows {score: 累计人数}, top_is_open)"""
    rows, open_top = {}, False
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.reader(fh)
        header = [h.strip() for h in next(reader)]
        try:
            ci = next(i for i, h in enumerate(header) if h in CUM_HEADERS)
            si = header.index(SCORE_HEADER)
        except (StopIteration, ValueError):
            raise ValueError(f"{path.name}: 表头缺少分数或累计人数列 —— {header}")
        for i, line in enumerate(reader):
            if not line or si >= len(line) or not line[si].strip():
                continue
            raw = line[si].strip()
            m = re.match(r"^(\d+)", raw)
            if not m:
                raise ValueError(f"{path.name}: 无法解析分数 {raw!r}")
            if i == 0 and OPEN_TOP.search(raw):
                open_top = True
            score = int(m.group(1))
            cum = int((line[ci] or "0").strip().replace(",", "") or 0)
            if score in rows and rows[score] != cum:
                raise ValueError(f"{path.name}: 分数 {score} 出现两次且人数不同")
            rows[score] = cum
    return rows, open_top


def densify(rows, top, base):
    """分数缺席即该分无人，累计人数与高一分相同。自高分向低分填充。

    只覆盖 [base, top]。base 是该年逐分公布到的最低分 —— 低于它的分数没有
    数据，绝不向下填充伪造，否则整段会被压成同一个位次。
    """
    cum, run = [], rows[top]
    for score in range(top, base - 1, -1):
        run = rows.get(score, run)
        cum.append(run)
    cum.reverse()  # index 0 == base
    return cum


def read_baselines():
    """绥化市高考参照分数。空单元格表示该年没有记录，不是 0。

    只保留至少有一个绥化数字的年份 —— 表里 2020 年以后几行目前只有一个
    看起来是填充下来的清华线，没有绥化数据，先不进入页面。
    """
    if not BASELINES.exists():
        return []
    out = []
    with BASELINES.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            year = (row.get("年份") or "").strip()
            if not year.isdigit():
                continue
            def num(key):
                v = (row.get(key) or "").strip().replace(",", "")
                return int(v) if v.isdigit() else None
            city, school = num("绥化市最高分"), num("绥化一中最高分")
            qinghua = num("清华分数线")
            jiaoda, zheda = num("上海交大分数线"), num("浙大分数线")
            if city is None and school is None and qinghua is None:
                continue
            yr = int(year)
            second_name = "浙大" if yr >= SECOND_TIER_SWITCH else "交大"
            second = zheda if yr >= SECOND_TIER_SWITCH else jiaoda
            if qinghua is not None and second is not None and second > qinghua:
                raise ValueError(
                    f"baselines.csv: {year} 年{second_name}线 {second} 高于清华线 {qinghua}")
            out.append({"year": yr, "qinghua": qinghua,
                        "jiaoda": jiaoda, "zheda": zheda,
                        "second": second, "secondName": second_name,
                        "city": city, "school": school})
    out.sort(key=lambda r: r["year"])
    return out


def read_school_top():
    """绥化一中历届前十的分数。表是稀疏的 —— 有的年份只留下前一两名，
    2007 年还缺第 4、5 名，缺的就是缺的，不补。"""
    if not SCHOOL_TOP.exists():
        return []
    out = []
    with SCHOOL_TOP.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            vals = [(row.get(k) or "").strip() for k in ("年份", "全校排名", "分数")]
            if not all(v.isdigit() for v in vals):
                continue
            year, rank, score = (int(v) for v in vals)
            out.append({"year": year, "rank": rank, "score": score})
    out.sort(key=lambda r: (r["year"], r["rank"]))

    # 同一年同一名次不该出现两次
    seen = set()
    for r in out:
        key = (r["year"], r["rank"])
        if key in seen:
            raise ValueError(f"suihua.csv: {r['year']} 年第 {r['rank']} 名重复")
        seen.add(key)
    return out


def fill_from_top(baselines, city_top, school_top):
    """绥化市/一中最高分就是各自前十榜的第一名 —— 两处数据必须一致。

    baselines.csv 留空时用榜首补齐（2006/2009 的市最高分即如此），
    两边都有却对不上则直接报错，免得页面上两个区块自相矛盾。
    """
    first = {}
    for rows, key in ((city_top, "city"), (school_top, "school")):
        for r in rows:
            if r["rank"] == 1 and r.get("score") is not None:
                first[(key, r["year"])] = r["score"]

    filled, conflicts = [], []
    for b in baselines:
        for key, label in (("city", "绥化市最高分"), ("school", "绥化一中最高分")):
            top = first.get((key, b["year"]))
            if top is None:
                continue
            if b[key] is None:
                b[key] = top
                filled.append(f"{b['year']} 年{label} ← 榜首 {top}")
            elif b[key] != top:
                conflicts.append(
                    f"{b['year']} 年{label}：baselines.csv 是 {b[key]}，"
                    f"前十榜第一名是 {top} —— 采用后者")
                b[key] = top
    return filled, conflicts


def cross_check_top(city_top, school_top, home="绥化一中"):
    """suihua.csv 与 suihuashi.csv 里的绥化一中学生应当是同一批人。

    市榜只收前十，校榜可能更长，所以只比对两边都覆盖到的那几个分数。
    对不上时报警而不中断 —— 数据以外的判断留给人。
    """
    warn = []
    by_year = {}
    for r in city_top:
        if r["score"] is not None and r["abbr"] == home:
            by_year.setdefault(r["year"], []).append(r["score"])
    school = {}
    for r in school_top:
        if r["score"] is not None:
            school.setdefault(r["year"], []).append(r["score"])
    for year, from_city in by_year.items():
        a = sorted(school.get(year, []), reverse=True)
        b = sorted(from_city, reverse=True)
        n = min(len(a), len(b))
        if n and a[:n] != b[:n]:
            warn.append(f"{year} 年{home}：suihua.csv 记为 {a[:n]}，"
                        f"suihuashi.csv 的市榜里记为 {b[:n]}")
    return warn


def read_city_top():
    """绥化市历届前十。分数一列可能是 '-'（只知道名次与学校，没留下分数），
    校名也可能缺失；两者都按缺失处理，不猜。"""
    if not CITY_TOP.exists():
        return []
    out, seen = [], set()
    with CITY_TOP.open(encoding="utf-8-sig", newline="") as fh:
        for row in csv.DictReader(fh):
            year = (row.get("年份") or "").strip()
            rank = (row.get("全市排名") or "").strip()
            if not (year.isdigit() and rank.isdigit()):
                continue
            score = (row.get("分数") or "").strip()
            school = (row.get("高中") or "").strip()
            key = (int(year), int(rank))
            if key in seen:
                raise ValueError(f"suihuashi.csv: {year} 年第 {rank} 名重复")
            seen.add(key)
            out.append({
                "year": int(year), "rank": int(rank),
                "score": int(score) if score.isdigit() else None,
                "school": school if school and school != "-" else "",
                "abbr": abbrev_school(school),
            })
    out.sort(key=lambda r: (r["year"], r["rank"]))
    return out


def build():
    years = []
    for path in sorted(SRC_DIR.glob("*.csv")):
        if not YEAR_FILE.match(path.stem):
            continue
        year = int(path.stem)
        rows, open_top = read_year(path)

        # 表首的虚拟锚点（累计 0 人）不是真实分数，剔除后再定上限
        real = {s: c for s, c in rows.items() if c > 0}
        if not real:
            raise ValueError(f"{path.name}: 全表累计人数为 0")
        top = max(real)
        published_floor = min(rows)

        base = max(FLOOR, published_floor)
        cum = densify(rows, top, base)
        for a, b in zip(cum, cum[1:]):
            if b > a:
                raise ValueError(f"{year}: 累计人数随分数下降而减少，数据有误")

        est = ESTIMATED_TOTAL.get(year) if published_floor > FLOOR else None
        if published_floor <= FLOOR:
            total = cum[0]
        elif est:
            total = est["total"]
            # 估计的分母必须大于表内已知的最低段累计人数
            if total <= cum[0]:
                raise ValueError(f"{year}: 估计分母 {total} 不大于 ≥{published_floor} 的 {cum[0]}")
        else:
            raise ValueError(f"{year}: 表止于 {published_floor} 分，且未配置估计分母")

        years.append({
            "year": year,
            "track": "物理类" if year >= NEW_GAOKAO_FROM else "理科",
            "top": top,
            "openTop": open_top,
            "base": base,                  # cum[0] 对应的分数
            "floor": published_floor,      # 该年逐分公布到的最低分
            "modelled": year in MODELLED,
            "total": total,
            "estimated": bool(est),
            "estBasis": est["basis"] if est else "",
            "estError": est["uncertainty"] if est else 0,
            "cum": cum,                    # cum[i] = 得分 >= (base+i) 的人数
        })
    years.sort(key=lambda y: y["year"])
    return years


def run(check=False, quiet=False):
    """跑一次完整构建。返回本次遇到的 ⚠ 条数（0 表示数据自洽）。"""
    say = (lambda *a: None) if quiet else print
    warnings = []

    years = build()
    say(f"{'年份':<6}{'科类':<6}{'逐分范围':<14}{'考生数(≥150)':>14}  备注")
    for y in years:
        note = []
        if y["estimated"]:
            note.append(f"分母估计 ±{y['estError']*100:g}%（表止于 {y['floor']} 分）")
        if y["openTop"]:
            note.append("顶端封口")
        if y["modelled"]:
            note.append("分数段推算")
        say(f"{y['year']:<6}{y['track']:<5}{y['base']}-{y['top']:<9}"
              f"{y['total']:>13,}  {'；'.join(note)}")
    say(f"\n共 {len(years)} 年"
          f"，其中 {sum(1 for y in years if y['estimated'])} 年分母为估计值")

    baselines = read_baselines()
    say("绥化参照：" + "；".join(
        f"{b['year']} 清华 {b['qinghua'] or '—'}／{b['secondName']} {b['second'] or '—'}"
        for b in baselines))


    school_top = read_school_top()
    per_year = {}
    for r in school_top:
        per_year.setdefault(r["year"], []).append(r["rank"])
    say("一中前十：" + "；".join(
        f"{y} 年 {len(v)} 条（第 {min(v)}–{max(v)} 名）" for y, v in sorted(per_year.items())))

    city_top = read_city_top()
    filled, conflicts = fill_from_top(baselines, city_top, school_top)
    for line in filled:
        say(f"  补齐：{line}")
    for line in conflicts + cross_check_top(city_top, school_top):
        warnings.append(line)
        print(f"  ⚠ 冲突：{line}")
    cy = {}
    for r in city_top:
        cy.setdefault(r["year"], []).append(r)
    say("全市前十：" + "；".join(
        f"{y} 年 {len(v)} 条（{sum(1 for r in v if r['score'] is not None)} 条有分数）"
        for y, v in sorted(cy.items())))
    schools = sorted({r["abbr"] for r in city_top if r["abbr"]})
    say(f"涉及中学 {len(schools)} 所：{'、'.join(schools)}")

    if check:
        say("（--check：未写文件）")
        return warnings


    payload = json.dumps({
        "floor": FLOOR,
        "defaultYear": DEFAULT_YEAR,
        "defaultScore": DEFAULT_SCORE,
        "years": years,
        "suihua": baselines,
        "schoolTop": school_top,
        "cityTop": city_top,
    }, ensure_ascii=False, separators=(",", ":"))
    html = TEMPLATE.read_text(encoding="utf-8").replace("__DATA__", payload)
    for out in OUTPUTS:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(html, encoding="utf-8")
        print(f"写入 {out.relative_to(ROOT)}  ({len(html)/1024:.0f} KB)")
    if warnings:
        print(f"⚠ 本次有 {len(warnings)} 处数据对不上（见上），页面已按现有数据生成。")
    return warnings


def watched_files():
    """每次重新 glob —— 新增或删除 CSV 也要能被 --watch 看见。"""
    yield from SRC_DIR.glob("*.csv")
    yield TEMPLATE
    yield Path(__file__)


def snapshot():
    """被监视文件的 (路径, mtime) 集合。"""
    return {(f, f.stat().st_mtime) for f in watched_files() if f.exists()}


def main():
    ap = argparse.ArgumentParser(
        description="从 content/2007/convert/*.csv 生成高考等位分换算页面。")
    ap.add_argument("--check", action="store_true", help="只解析并报告，不写文件")
    ap.add_argument("--watch", action="store_true", help="盯着 CSV 与模板，改动即重新生成")
    ap.add_argument("--quiet", "-q", action="store_true", help="只打印警告与写入结果")
    ap.add_argument("--strict", action="store_true", help="有 ⚠ 时以退出码 1 结束")
    args = ap.parse_args()

    if not args.watch:
        warnings = run(check=args.check, quiet=args.quiet)
        sys.exit(1 if (args.strict and warnings) else 0)

    sys.stdout.reconfigure(line_buffering=True)   # 重定向到文件时也要能实时看到
    print(f"监视 {SRC_DIR.relative_to(ROOT)}/*.csv 与模板，Ctrl-C 结束。")
    last = None
    try:
        while True:
            now = snapshot()
            if now != last:
                if last is not None:
                    print(f"\n—— {time.strftime('%H:%M:%S')} 检测到改动，重新生成 ——")
                try:
                    run(check=args.check, quiet=args.quiet or last is not None)
                except Exception as e:          # 数据写坏了不该让 watch 退出
                    print(f"✗ 生成失败：{type(e).__name__}: {e}")
                last = now
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n结束。")


if __name__ == "__main__":
    main()
