"""Regenerate the two 「每出一个 600 分以上需考生数」 bar charts in
scripts/suihua-template.html → #sec-2004.

    python3 scripts/gen-suihua-sec2004-figs.py            # print both SVGs
    python3 scripts/gen-suihua-sec2004-figs.py --year 2007

The SVGs are hand-pasted into the template between the <div class="figwrap">
markers (there is no placeholder substitution — paste, then run
scripts/build-suihua.py). Geometry copies the original chart: row pitch 25,
bar height 15, bars start at x=94, left axis line at x=90, the 全省 average
drawn as a red dashed line.

2004 data — content/2004/2004年黑龙江省各地市高考600分以上与650分以上人数统计（官方分市表）.csv
2007 data — content/2004/2007年黑龙江分地市高考考生数与600分以上人数.csv
             (绥化/全省 实测; 大庆/鹤岗 考生数为网络存档夹逼估计; 其余待补)
"""

import argparse
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_2004 = ROOT / "content/2004/2004年黑龙江省各地市高考600分以上与650分以上人数统计（官方分市表）.csv"
CSV_2007 = ROOT / "content/2004/2007年黑龙江分地市高考考生数与600分以上人数.csv"

X0, PITCH, BARH, TOP, AXIS_X, VIEWW = 94, 25, 15, 24, 90, 980


def hbar(items, prov_per, *, scale, me, estimate, aria, footnote, band="600"):
    """items: list of (name, per, total, hi). prov_per: 全省 每出一个."""
    parts = [f'<line x1="{AXIS_X}" y1="12" x2="{AXIS_X}" y2="__AB__" '
             f'stroke="var(--rule)" stroke-width="1"/>']
    px = X0 + prov_per * scale
    parts.append(
        f'<line x1="{px:.1f}" y1="12" x2="{px:.1f}" y2="__AB__" stroke="var(--seal)" '
        f'stroke-width="1" stroke-dasharray="4 3"/>'
        f'<text class="cax" x="{px + 4:.1f}" y="10" style="fill:var(--seal)">'
        f'全省 {prov_per:,.0f}</text>')
    y = TOP
    for name, v, total, hi in sorted(items, key=lambda r: r[1]):
        w = v * scale
        is_me, is_est = name == me, name in estimate
        lc = "var(--seal)" if is_me else "var(--ink-2)"
        lw = "font-weight:700;" if is_me else ""
        parts.append(f'<text class="cax" x="86" y="{y + 12}" text-anchor="end" '
                     f'style="font-size:12.5px;{lw}fill:{lc}">{name}</text>')
        fill = "var(--seal)" if is_me else "var(--mark-gray)"
        est = (' stroke="var(--ink-3)" stroke-width="1" stroke-dasharray="3 2" '
               'fill-opacity="0.45"') if is_est else ""
        title = (f'{name}：{v:,.0f} 名考生产生 1 名 {band} 分以上'
                 f'（{total:,} 考生／{hi:,} 人）'
                 + ('（考生数为估计值）' if is_est else ''))
        parts.append(f'<rect x="{X0}" y="{y}" width="{w:.1f}" height="{BARH}" rx="2" '
                     f'fill="{fill}"{est}><title>{title}</title></rect>')
        vc = "var(--seal)" if is_me else "var(--ink-3)"
        vw = "font-weight:600;" if is_me else ""
        vtxt = (f'{v:,.0f} 人／个　（{total:,} 考生，{hi:,} 人上线）' if not is_est
                else f'约 {v:,.0f} 人／个　（考生数约 {total:,}〔估〕，{hi:,} 人上线）')
        parts.append(f'<text class="cax" x="{X0 + w + 8:.1f}" y="{y + 12}" '
                     f'style="{vw}fill:{vc}">{vtxt}</text>')
        y += PITCH
    ab = y + 4
    parts.append(f'<text class="cax" x="{AXIS_X}" y="{ab + 18}">{footnote}</text>')
    body = "".join(parts).replace("__AB__", str(ab))
    return (f'<svg viewBox="0 0 {VIEWW} {ab + 28}" width="100%" role="img" '
            f'aria-label="{aria}">{body}</svg>')


def rows_2004(col="600分以上人数"):
    out, prov = [], None
    for r in csv.DictReader(CSV_2004.open(encoding="utf-8-sig")):
        if not r[col].strip():          # 黑河 / 大兴安岭 have no 650+ figure
            continue
        tot, hi = int(r["报名总人数"]), int(r[col])
        rec = (r["地市"].replace("全省合计", "全省"), tot / hi, tot, hi)
        if r["地市"] == "全省合计":
            prov = rec
        else:
            out.append(rec)
    return out, prov[1]


def rows_2007():
    out, prov = [], None
    for r in csv.DictReader(CSV_2007.open(encoding="utf-8-sig")):
        if not r["高考报名人数"] or not r["合计600分以上"]:
            continue
        tot, hi = int(r["高考报名人数"]), int(r["合计600分以上"])
        rec = (r["地市"], tot / hi, tot, hi)
        if r["地市"] == "全省":
            prov = rec
        else:
            out.append(rec)
    return out, prov[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--year", choices=["2004", "2007", "both"], default="both")
    args = ap.parse_args()

    if args.year in ("2004", "both"):
        items, prov = rows_2004("600分以上人数")
        print("# 2004 —— 每出一个 600 需（升序）")
        for n, v, t, h in sorted(items, key=lambda r: r[1]):
            print(f"#   {n:6s} {v:6.1f}  ({t:,}/{h})")
        print(hbar(items, prov, scale=1.9, me="绥化", estimate=set(),
                   aria="2004年黑龙江各地市每产生一名600分以上考生所需的考生数",
                   footnote="柱长＝每出一个 600+ 所需考生数　·　红虚线＝全省平均（87）。"
                            "越长＝越难出高分。"))
        print()

        items, prov = rows_2004("650分以上人数")
        print("# 2004 —— 每出一个 650 需（升序）")
        for n, v, t, h in sorted(items, key=lambda r: r[1]):
            print(f"#   {n:6s} {v:8.1f}  ({t:,}/{h})")
        print(hbar(items, prov, scale=0.105, me="绥化", estimate=set(), band="650",
                   aria="2004年黑龙江各地市每产生一名650分以上考生所需的考生数",
                   footnote="柱长＝每出一个 650+ 所需考生数　·　红虚线＝全省平均（1,013）。"
                            "同一批人，同一张卷子——只是把线从 600 抬到 650。"))
        print()

    if args.year in ("2007", "both"):
        items, prov = rows_2007()
        est = {n for n, *_ in items} - {"绥化全市"}
        print("# 2007 —— 每出一个 600 需")
        for n, v, t, h in sorted(items, key=lambda r: r[1]):
            print(f"#   {n:8s} {v:6.1f}  ({t:,}/{h})")
        print(hbar(items, prov, scale=13.5, me="绥化全市", estimate=est,
                   aria="2007年绥化、大庆、鹤岗每产生一名600分以上考生所需的考生数",
                   footnote="柱长＝每出一个 600+ 所需考生数　·　红虚线＝全省平均。"
                            "绥化、全省为实测；大庆、鹤岗的考生数为估计。"))


if __name__ == "__main__":
    main()
