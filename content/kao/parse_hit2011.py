#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Parse 2011 HIT graduation list. Line-by-line approach, more robust.
"""

import re, csv, sys
from collections import OrderedDict

with open('hit2011_layout.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

# ── helpers ──────────────────────────────────────────────────────────────────
def compact(s):
    return re.sub(r'\s+', '', s)

def is_name(s):
    c = compact(s)
    return bool(re.fullmatch(r'[\u4e00-\u9fff]{2,4}', c))

# ── college patterns (must NOT be stripped by our name regex) ─────────────────
COLLEGES = [
    (r'航\s*天\s*学\s*院',            '航天学院'),
    (r'电\s*子\s*与\s*信\s*息\s*工\s*程\s*学\s*院', '电子与信息工程学院'),
    (r'机\s*电\s*工\s*程\s*学\s*院',  '机电工程学院'),
    (r'材\s*料\s*科\s*学\s*与\s*工\s*程\s*学\s*院', '材料科学与工程学院'),
    (r'能\s*源\s*科\s*学\s*与\s*工\s*程\s*学\s*院', '能源科学与工程学院'),
    (r'电\s*气\s*工\s*程\s*及\s*(其\s*)?自\s*动\s*化\s*学\s*院', '电气工程及自动化学院'),
    (r'理\s*学\s*院',                 '理学院'),
    (r'生\s*命\s*科\s*学\s*与\s*技\s*术\s*学\s*院', '生命科学与技术学院'),
    (r'经\s*济\s*与\s*管\s*理\s*学\s*院', '经济与管理学院'),
    (r'人\s*文\s*与\s*社\s*会\s*科\s*学\s*学\s*院', '人文与社会科学学院'),
    (r'土\s*木\s*工\s*程\s*学\s*院',  '土木工程学院'),
    (r'市\s*政\s*环\s*境\s*工\s*程\s*学\s*院', '市政环境工程学院'),
    (r'建\s*筑\s*学\s*院',            '建筑学院'),
    (r'交\s*通\s*科\s*学\s*与\s*工\s*程\s*学\s*院', '交通科学与工程学院'),
    (r'计\s*算\s*机\s*科\s*学\s*与\s*技\s*术\s*学\s*院', '计算机科学与技术学院'),
    (r'软\s*件\s*学\s*院',            '软件学院'),
    (r'法\s*学\s*院',                 '法学院'),
    (r'外\s*国\s*语\s*学\s*院',       '外国语学院'),
    (r'化\s*工\s*学\s*院',            '化工学院'),
    (r'食\s*品\s*科\s*学\s*与\s*工\s*程\s*学\s*院', '食品科学与工程学院'),
    (r'媒\s*体\s*技\s*术\s*与\s*艺\s*术\s*系', '媒体技术与艺术系'),
    (r'英\s*才\s*学\s*院',            '英才学院'),
    (r'哈\s*尔\s*滨\s*工\s*业\s*大\s*学\s*威\s*海', '哈尔滨工业大学威海校区'),
]

# Major name: a line whose compacted form ends with 专业 and is not too long
# Compile known major names with their canonical forms
KNOWN_MAJORS = {
    compact(k): v for k, v in [
        ('自动化专业', '自动化专业'),
        ('探测制导与控制技术专业', '探测制导与控制技术专业'),
        ('工程力学专业', '工程力学专业'),
        ('飞行器设计与工程专业', '飞行器设计与工程专业'),
        ('电子科学与技术专业', '电子科学与技术专业'),
        ('电子信息科学与技术专业', '电子信息科学与技术专业'),
        ('复合材料与工程专业', '复合材料与工程专业'),
        ('空间科学与技术专业', '空间科学与技术专业'),
        ('电子信息工程专业', '电子信息工程专业'),
        ('通信工程专业', '通信工程专业'),
        ('信息对抗技术专业', '信息对抗技术专业'),
        ('光学专业', '光学专业'),  # 廳科学
        ('光科学与技术专业', '光科学与技术专业'),
        ('机械设计制造及其自动化专业', '机械设计制造及其自动化专业'),
        ('工业工程专业', '工业工程专业'),
        ('飞行器制造工程专业', '飞行器制造工程专业'),
        ('工业设计专业', '工业设计专业'),
        ('材料成型及控制工程专业', '材料成型及控制工程专业'),
        ('材料科学与工程专业', '材料科学与工程专业'),
        ('焊接技术与工程专业', '焊接技术与工程专业'),
        ('材料化学专业', '材料化学专业'),
        ('电子封装技术专业', '电子封装技术专业'),
        ('光信息科学与技术专业', '光信息科学与技术专业'),
        ('软件工程专业', '软件工程专业'),
        ('土木工程专业', '土木工程专业'),
        ('船舶与海洋工程专业', '船舶与海洋工程专业'),
        ('热能与动力工程专业', '热能与动力工程专业'),
        ('核反应堆工程', '核反应堆工程专业'),
        ('飞行器动力工程专业', '飞行器动力工程专业'),
        ('电气工程及其自动化专业', '电气工程及其自动化专业'),
        ('测控技术与仪器专业', '测控技术与仪器专业'),
        ('光电信息工程专业', '光电信息工程专业'),
        ('应用化学专业', '应用化学专业'),
        ('材料化学专业', '材料化学专业'),
        ('应用物理学专业', '应用物理学专业'),
        ('数学与应用数学专业', '数学与应用数学专业'),
        ('信息与计算科学专业', '信息与计算科学专业'),
        ('核化工与核燃料工程', '核化工与核燃料工程专业'),
        ('核物理', '核物理专业'),
        ('生物技术专业', '生物技术专业'),
        ('生物工程专业', '生物工程专业'),
        ('信息管理与信息系统专业', '信息管理与信息系统专业'),
        ('工商管理专业', '工商管理专业'),
        ('市场营销专业', '市场营销专业'),
        ('会计学专业', '会计学专业'),
        ('金融学专业', '金融学专业'),
        ('国际经济与贸易专业', '国际经济与贸易专业'),
        ('工程管理专业', '工程管理专业'),
        ('财务管理专业', '财务管理专业'),
        ('社会学专业', '社会学专业'),
        ('法学专业', '法学专业'),
        ('英语专业', '英语专业'),
        ('俄语专业', '俄语专业'),
        ('日语专业', '日语专业'),
        ('高分子材料与工程专业', '高分子材料与工程专业'),
        ('化学工程与工艺专业', '化学工程与工艺专业'),
        ('食品科学与工程专业', '食品科学与工程专业'),
        ('广播电视编导专业', '广播电视编导专业'),
        ('广告学专业', '广告学专业'),
        ('建筑学专业', '建筑学专业'),
        ('艺术设计专业', '艺术设计专业'),
        ('城市规划专业', '城市规划专业'),
        ('交通工程专业', '交通工程专业'),
        ('交通运输专业', '交通运输专业'),
        ('道路桥梁与渡河工程专业', '道路桥梁与渡河工程专业'),
        ('给水排水工程专业', '给水排水工程专业'),
        ('环境工程专业', '环境工程专业'),
        ('环境科学专业', '环境科学专业'),
        ('建筑环境与设备工程专业', '建筑环境与设备工程专业'),
        ('理论与应用力学专业', '理论与应用力学专业'),
        ('计算机科学与技术专业', '计算机科学与技术专业'),
        ('生物信息技术专业', '生物信息技术专业'),
        ('信息安全专业', '信息安全专业'),
        ('汉语言文学专业', '汉语言文学专业'),
        ('车辆工程专业', '车辆工程专业'),
        ('测控技术与仪器专业', '测控技术与仪器专业'),
        ('给排水科学与工程专业', '给排水科学与工程专业'),
    ]
}

def try_college(line_compact):
    for pat, name in COLLEGES:
        if re.search(pat, line_compact):
            return name
    return None

def try_major(line_compact, raw_line):
    # Check known majors dict
    if line_compact in KNOWN_MAJORS:
        return KNOWN_MAJORS[line_compact]
    # Generic: ends with 专业 and ≤ 15 chars
    if line_compact.endswith('专业') and len(line_compact) <= 15:
        return line_compact
    # Ends with 工程 (but not compound with other text)
    if re.fullmatch(r'[\u4e00-\u9fff]{4,12}工\s*程', line_compact):
        return line_compact + '专业'
    # Core keywords like 核物理, 核反应堆工程
    if re.fullmatch(r'[\u4e00-\u9fff]{3,8}', line_compact) and any(
            k in line_compact for k in ['物理', '化学', '数学', '工程', '技术', '科学']):
        return line_compact + '专业'
    return None

# ── Page-level parsing ───────────────────────────────────────────────────────
records = []
current_college = '航天学院'   # first college in document
current_major   = ''

# Strip page-break chars and junk header lines
# Page junk: lines matching year/page patterns
JUNK = re.compile(
    r'^\s*(?:'
    r'[１２０-９]{4,}|'          # page numbers like ２２４
    r'哈\s*尔\s*滨\s*工\s*业\s*大\s*学\s*年\s*鉴|'
    r'毕\s*业\s*生\s*及\s*出\s*站\s*博\s*士\s*后|'
    r'普\s*通\s*本|'
    r'[Ｚ＼，＾Ｙ＂＇]{1}|'
    r'[￣—=＝]{2,}|'
    r'\s*\f\s*'
    r')\s*$',
    re.MULTILINE
)

lines = raw.split('\n')

i = 0
while i < len(lines):
    line = lines[i]
    c = compact(line)
    i += 1

    if not c:
        continue

    # Skip junk
    if JUNK.match(line):
        continue
    # Skip lines that are page header patterns
    if re.search(r'[Ｚ＼＾Ｙ]', line):
        continue
    if re.search(r'[￣—]{2,}', line):
        continue
    if re.search(r'２０１２', c):
        continue

    # Check college
    col = try_college(c)
    if col:
        current_college = col
        continue

    # Check major – line must consist nearly entirely of Chinese + spaces,
    # be relatively short, and end with 专业 or known suffix
    # Filter: line should not have too many chars (likely a name line if > 30 compact chars)
    if len(c) <= 18:
        maj = try_major(c, line)
        if maj:
            current_major = maj
            continue

    # Otherwise extract names from this line
    if not current_major:
        continue

    # Split line by 2+ spaces or tabs
    parts = re.split(r'[ \t]{2,}', line)
    for part in parts:
        part = part.strip()
        pc = compact(part)
        if is_name(pc):
            # Skip header-like words
            if pc in {'专业', '学院', '毕业', '出站', '博士', '普通', '名单',
                      '年鉴', '哈尔', '滨工', '大学', '及出', '站博', '士后',
                      '本专', '科毕', '工程', '技术', '科学'}:
                continue
            records.append({
                'college': current_college,
                'major': current_major,
                'name': pc,
            })

# De-duplicate (same college+major+name)
seen = set()
unique = []
for r in records:
    key = (r['college'], r['major'], r['name'])
    if key not in seen:
        seen.add(key)
        unique.append(r)

print(f"Total records: {len(unique)}", file=sys.stderr)

# ── CSV ────────────────────────────────────────────────────────────────────────
csv_path = '2011年哈尔滨工业大学普通本、专科毕业生名单.csv'
with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=['序号', '学院', '专业', '姓名'])
    w.writeheader()
    for idx, r in enumerate(unique, 1):
        w.writerow({'序号': idx, '学院': r['college'], '专业': r['major'], '姓名': r['name']})
print(f"CSV: {csv_path}", file=sys.stderr)

# ── HTML ───────────────────────────────────────────────────────────────────────
from collections import OrderedDict

college_data = OrderedDict()
for r in unique:
    c, m = r['college'], r['major']
    college_data.setdefault(c, OrderedDict()).setdefault(m, []).append(r['name'])

total = len(unique)
n_colleges = len(college_data)
n_majors   = sum(len(m) for m in college_data.values())
college_counts = {c: sum(len(v) for v in ms.values()) for c, ms in college_data.items()}

# Build college options HTML
college_opts = '\n'.join(
    f'      <option value="{c}">{c}（{college_counts[c]}人）</option>'
    for c in college_data
)

# Build card sections
icons = ['🏛','🔬','⚡','🛸','🔧','📡','🌊','🏗','🚀','💻',
         '📐','🧬','📊','🌿','🎓','⚗','🍎','📺','🔭','🏛','🎨','🚗','🌐']
card_html = ''
for idx, (college, majors) in enumerate(college_data.items()):
    icon = icons[idx % len(icons)]
    cnt  = college_counts[college]
    card_html += f'  <section class="college-section" data-college="{college}">\n'
    card_html += f'    <div class="college-header"><div class="college-icon">{icon}</div><div class="college-name">{college}</div><div class="college-count">{cnt} 人</div></div>\n'
    for major, names in majors.items():
        card_html += f'    <div class="major-block" data-major="{major}">\n'
        card_html += f'      <div class="major-header" onclick="toggleMajor(this.parentElement)"><span class="major-title">{major}</span><span class="major-badge">{len(names)} 人</span><span class="major-toggle">▼</span></div>\n'
        card_html += '      <div class="names-grid">\n'
        for name in names:
            card_html += f'        <div class="name-chip" data-name="{name}">{name}</div>\n'
        card_html += '      </div>\n    </div>\n'
    card_html += '  </section>\n'

# Build table rows
table_rows = ''
for idx, r in enumerate(unique, 1):
    table_rows += (f'        <tr data-college="{r["college"]}" data-major="{r["major"]}" data-name="{r["name"]}">'
                   f'<td>{idx}</td><td class="td-college">{r["college"]}</td>'
                   f'<td class="td-major">{r["major"]}</td><td>{r["name"]}</td></tr>\n')

html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>2011年哈尔滨工业大学普通本、专科毕业生名单</title>
<meta name="description" content="2011年哈尔滨工业大学普通本科及专科毕业生完整名单，共{total}人，按学院和专业分类。">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root{{
  --bg:#0f1117;--bg-card:#181c27;--bg-card2:#1e2235;
  --gold:#c8a96e;--gold2:#e8c98a;--gold-dim:rgba(200,169,110,.15);
  --text:#e8e4d8;--muted:#8a8578;--dim:#5a5650;
  --border:rgba(200,169,110,.22);--border-dim:rgba(255,255,255,.06);
  --radius:12px;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Inter','Noto Serif SC',sans-serif;background:var(--bg);color:var(--text);min-height:100vh;line-height:1.6}}

/* HERO */
.hero{{background:linear-gradient(135deg,#0a0e1a,#131929 60%,#0f1520);border-bottom:1px solid var(--border);padding:60px 24px 48px;text-align:center;position:relative;overflow:hidden}}
.hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 0%,rgba(200,169,110,.08),transparent 70%);pointer-events:none}}
.badge{{display:inline-block;background:var(--gold-dim);border:1px solid var(--border);color:var(--gold);font-size:11px;font-weight:600;letter-spacing:2px;text-transform:uppercase;padding:6px 16px;border-radius:999px;margin-bottom:24px}}
.hero h1{{font-family:'Noto Serif SC',serif;font-size:clamp(20px,4vw,34px);font-weight:700;color:#fff;letter-spacing:2px;margin-bottom:10px}}
.hero-sub{{color:var(--muted);font-size:13px;margin-bottom:32px}}
.stats{{display:flex;justify-content:center;gap:40px;flex-wrap:wrap}}
.stat-num{{font-size:32px;font-weight:700;color:var(--gold);line-height:1}}
.stat-label{{font-size:11px;color:var(--muted);margin-top:4px;letter-spacing:1px}}

/* CONTROLS */
.controls{{position:sticky;top:0;z-index:100;background:rgba(15,17,23,.94);backdrop-filter:blur(12px);border-bottom:1px solid var(--border-dim);padding:14px 24px}}
.ctrl{{max-width:1200px;margin:0 auto;display:flex;gap:10px;align-items:center;flex-wrap:wrap}}
.sw{{flex:1;min-width:180px;position:relative}}
.sw svg{{position:absolute;left:11px;top:50%;transform:translateY(-50%);color:var(--dim);pointer-events:none}}
#search{{width:100%;background:var(--bg-card);border:1px solid var(--border-dim);border-radius:8px;color:var(--text);font-size:14px;padding:9px 11px 9px 36px;outline:none;transition:border .2s}}
#search:focus{{border-color:var(--gold)}}
#search::placeholder{{color:var(--dim)}}
select{{background:var(--bg-card);border:1px solid var(--border-dim);border-radius:8px;color:var(--text);font-size:13px;padding:9px 11px;outline:none;cursor:pointer;min-width:130px}}
select:focus{{border-color:var(--gold)}}
option{{background:#181c27}}
.rc{{font-size:13px;color:var(--muted);white-space:nowrap}}
.rc span{{color:var(--gold);font-weight:600}}
.vt{{display:flex;gap:3px;background:var(--bg-card);border:1px solid var(--border-dim);border-radius:8px;padding:3px}}
.vb{{background:none;border:none;color:var(--dim);padding:6px 10px;border-radius:5px;cursor:pointer;font-size:13px;transition:all .2s}}
.vb.active{{background:var(--gold);color:#0a0e1a;font-weight:700}}

/* MAIN */
.main{{max-width:1200px;margin:0 auto;padding:32px 24px 80px}}

/* COLLEGE */
.college-section{{margin-bottom:48px}}
.college-header{{display:flex;align-items:center;gap:14px;margin-bottom:18px;padding-bottom:12px;border-bottom:1px solid var(--border)}}
.ci{{width:40px;height:40px;background:var(--gold-dim);border:1px solid var(--border);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:17px;flex-shrink:0}}
.cn{{font-family:'Noto Serif SC',serif;font-size:19px;font-weight:600;color:var(--gold2);flex:1}}
.cc{{font-size:12px;color:var(--dim);background:var(--bg-card2);border:1px solid var(--border-dim);border-radius:6px;padding:3px 9px;white-space:nowrap}}

/* MAJOR */
.major-block{{background:var(--bg-card);border:1px solid var(--border-dim);border-radius:var(--radius);margin-bottom:12px;overflow:hidden;transition:border .2s}}
.major-block:hover{{border-color:rgba(200,169,110,.35)}}
.major-header{{display:flex;align-items:center;justify-content:space-between;padding:12px 18px;background:var(--bg-card2);cursor:pointer;user-select:none;gap:10px}}
.mt{{font-size:14px;font-weight:500;color:var(--text);flex:1}}
.mb{{font-size:12px;color:var(--gold);background:var(--gold-dim);border-radius:999px;padding:2px 9px;white-space:nowrap}}
.mg{{color:var(--dim);font-size:11px;transition:transform .3s}}
.major-block.collapsed .mg{{transform:rotate(-90deg)}}
.names-grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(68px,1fr));gap:7px;padding:14px 18px 18px}}
.major-block.collapsed .names-grid{{display:none}}
.nc{{background:var(--bg);border:1px solid var(--border-dim);border-radius:7px;padding:7px 3px;text-align:center;font-family:'Noto Serif SC',serif;font-size:14px;color:var(--text);cursor:default;transition:all .15s;white-space:nowrap}}
.nc:hover{{background:var(--gold-dim);border-color:var(--gold);color:var(--gold2)}}
.nc.hl{{background:var(--gold-dim);border-color:var(--gold);color:var(--gold2);animation:pop .5s ease}}
@keyframes pop{{0%,100%{{transform:scale(1)}}50%{{transform:scale(1.1)}}}}

/* TABLE */
.tw{{overflow-x:auto;border:1px solid var(--border-dim);border-radius:var(--radius)}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
thead th{{background:var(--bg-card2);color:var(--gold);font-weight:700;font-size:11px;letter-spacing:1px;text-transform:uppercase;padding:13px 15px;text-align:left;border-bottom:1px solid var(--border);position:sticky;top:0}}
tbody tr{{border-bottom:1px solid var(--border-dim);transition:background .15s}}
tbody tr:hover{{background:var(--bg-card)}}
tbody tr:last-child{{border-bottom:none}}
td{{padding:10px 15px;color:var(--text)}}
td:first-child{{color:var(--dim);font-size:12px;width:55px}}
td:last-child{{font-family:'Noto Serif SC',serif;font-size:15px}}
.tc{{color:var(--gold2);font-size:13px}}
.tm{{color:var(--muted);font-size:13px}}

.hidden{{display:none!important}}
footer{{text-align:center;padding:28px;color:var(--dim);font-size:12px;border-top:1px solid var(--border-dim)}}

@media(max-width:600px){{
  .hero{{padding:36px 14px 28px}}
  .stats{{gap:20px}}
  .main{{padding:18px 10px 60px}}
  .names-grid{{grid-template-columns:repeat(auto-fill,minmax(60px,1fr));gap:5px}}
}}
</style>
</head>
<body>

<section class="hero">
  <div class="badge">哈尔滨工业大学 · 2011届</div>
  <h1>普通本、专科毕业生名单</h1>
  <p class="hero-sub">《哈尔滨工业大学年鉴 2012》收录 · 本科及专科毕业生完整名录</p>
  <div class="stats">
    <div class="stat"><div class="stat-num" id="total-count">{total}</div><div class="stat-label">毕业生总数</div></div>
    <div class="stat"><div class="stat-num">{n_colleges}</div><div class="stat-label">学院数</div></div>
    <div class="stat"><div class="stat-num">{n_majors}</div><div class="stat-label">专业数</div></div>
  </div>
</section>

<div class="controls">
  <div class="ctrl">
    <div class="sw">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
      <input type="search" id="search" placeholder="搜索姓名、专业或学院…" autocomplete="off">
    </div>
    <select id="college-filter">
      <option value="">全部学院</option>
{college_opts}
    </select>
    <div class="vt">
      <button class="vb active" id="btn-card" onclick="setView('card')">卡片</button>
      <button class="vb" id="btn-table" onclick="setView('table')">列表</button>
    </div>
    <div class="rc">显示 <span id="shown-count">0</span> 人</div>
  </div>
</div>

<main class="main">
<div id="card-view">
{card_html}</div>

<div id="table-view" class="hidden">
  <div class="tw"><table>
    <thead><tr><th>序号</th><th>学院</th><th>专业</th><th>姓名</th></tr></thead>
    <tbody id="tb">
{table_rows}    </tbody>
  </table></div>
</div>
</main>

<footer>2011年哈尔滨工业大学普通本、专科毕业生名单 &nbsp;|&nbsp; 数据来源：《哈尔滨工业大学年鉴 2012》</footer>

<script>
let VIEW='card';
function setView(v){{
  VIEW=v;
  document.getElementById('card-view').classList.toggle('hidden',v!=='card');
  document.getElementById('table-view').classList.toggle('hidden',v!=='table');
  document.getElementById('btn-card').classList.toggle('active',v==='card');
  document.getElementById('btn-table').classList.toggle('active',v==='table');
  updateCount();
}}
function toggleMajor(b){{b.classList.toggle('collapsed');}}
function updateCount(){{
  let n=0;
  if(VIEW==='card') document.querySelectorAll('.nc:not(.hidden)').forEach(()=>n++);
  else document.querySelectorAll('#tb tr:not(.hidden)').forEach(()=>n++);
  document.getElementById('shown-count').textContent=n;
}}
function applyFilters(){{
  const q=document.getElementById('search').value.trim();
  const cf=document.getElementById('college-filter').value;
  document.querySelectorAll('.college-section').forEach(sec=>{{
    const col=sec.dataset.college;
    if(cf&&col!==cf){{sec.classList.add('hidden');return;}}
    sec.classList.remove('hidden');
    let sv=false;
    sec.querySelectorAll('.major-block').forEach(blk=>{{
      const maj=blk.dataset.major;
      let bv=false;
      blk.querySelectorAll('.nc').forEach(chip=>{{
        const nm=chip.dataset.name;
        const ok=!q||(nm.includes(q)||maj.includes(q)||col.includes(q));
        chip.classList.toggle('hidden',!ok);
        chip.classList.toggle('hl',!!q&&nm.includes(q));
        if(ok)bv=true;
      }});
      blk.classList.toggle('hidden',!bv);
      if(bv){{blk.classList.remove('collapsed');sv=true;}}
    }});
    sec.classList.toggle('hidden',!sv);
  }});
  document.querySelectorAll('#tb tr').forEach(tr=>{{
    const ok=(!cf||tr.dataset.college===cf)&&
             (!q||(tr.dataset.name.includes(q)||tr.dataset.major.includes(q)||tr.dataset.college.includes(q)));
    tr.classList.toggle('hidden',!ok);
  }});
  updateCount();
}}
document.getElementById('search').addEventListener('input',applyFilters);
document.getElementById('college-filter').addEventListener('change',applyFilters);
updateCount();
</script>
</body>
</html>'''

html_path = '2011年哈尔滨工业大学普通本、专科毕业生名单.html'
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)
print(f"HTML: {html_path}", file=sys.stderr)
print(f"Done! {len(unique)} records.", file=sys.stderr)
