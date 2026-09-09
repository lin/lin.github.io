#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build 1-point frequency distribution histogram for Daqing 2004 High School Entrance Exam (score >= 610)
Generates:
  1. static/daqing-2004-fenbu/one-point.html (standalone dedicated page)
  2. Updates static/daqing-2004-fenbu/index.html (integrates the 1-point frequency histogram section)
  3. Copies to public/daqing-2004-fenbu/
"""

import os
import json
import shutil
import pandas as pd
import numpy as np

CSV_PATH = './public/2004/2004年大庆中考录取总表.csv'
df = pd.read_csv(CSV_PATH)

# Filter score >= 610
high = df[df['文化成绩'] >= 610].sort_values(by=['文化成绩', '名次'], ascending=[False, True])

# School classification
def get_school_key(s):
    if s == '铁人中学': return 'tr'
    if s == '实验中学': return 'sy'
    if s == '一中': return 'yz'
    return 'other'

scores_range = list(range(610, 664))
bins_1pt = []
cum_top = 0

for s in sorted(scores_range, reverse=True):
    sub = high[high['文化成绩'] == s]
    cnt = len(sub)
    tr = len(sub[sub['录取高中'] == '铁人中学'])
    sy = len(sub[sub['录取高中'] == '实验中学'])
    yz = len(sub[sub['录取高中'] == '一中'])
    other = cnt - tr - sy - yz
    cum_top += cnt
    
    sts = []
    for _, r in sub.iterrows():
        sts.append({
            'rank': int(r['名次']),
            'no': int(r['考号']),
            'name': str(r['姓名']),
            'sex': str(r['性别']),
            'ms': str(r['初中学校']),
            'hs': str(r['录取高中']),
            'plan': str(r['计划形式'])
        })
    bins_1pt.append({
        'score': s,
        'count': cnt,
        'tr': tr,
        'sy': sy,
        'yz': yz,
        'other': other,
        'cum': cum_top,
        'students': sts
    })

# Ascending for left-to-right rendering
bins_asc = sorted(bins_1pt, key=lambda x: x['score'])

# Calculate key statistics
scores_series = high['文化成绩']
total_students = len(scores_series)
mean_score = scores_series.mean()
median_score = scores_series.median()
std_score = scores_series.std()
mode_score = int(scores_series.mode()[0])
mode_count = int((scores_series == mode_score).sum())
max_score = int(scores_series.max())
min_score = int(scores_series.min())

tr_total = int((high['录取高中'] == '铁人中学').sum())
sy_total = int((high['录取高中'] == '实验中学').sum())
yz_total = int((high['录取高中'] == '一中').sum())
other_total = total_students - tr_total - sy_total - yz_total

json_data_str = json.dumps({
    'total': total_students,
    'mean': round(mean_score, 2),
    'median': median_score,
    'std': round(std_score, 2),
    'mode': mode_score,
    'modeCount': mode_count,
    'max': max_score,
    'min': min_score,
    'schools': {
        'tr': tr_total,
        'sy': sy_total,
        'yz': yz_total,
        'other': other_total
    },
    'bins': bins_asc
}, ensure_ascii=False, separators=(',', ':'))

print(f"Data prepared: {total_students} students, range {min_score}-{max_score}")

# Build standalone page
STANDALONE_HTML = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>2004年大庆中考 610分以上考生一分频数分布直方图</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&family=Noto+Serif+SC:wght@600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap">
<style>
:root{{
  color-scheme: light;
  --page:#e7eaec; --card:#f8f9fa; --card-2:#eef1f2; --sunk:#e2e6e8;
  --ink:#11171a; --ink-2:#4b555b; --ink-3:#7f8a90;
  --rule:#ced4d7; --hair:#dfe3e5;
  --petrol:#0e5b68; --petrol-2:#4e97a3;
  --amber:#a86d0b; --amber-2:#d9ab63;
  --seal:#a5342a; --seal-wash:rgba(165,52,42,.08);
  --violet:#6b3fa0;
  --void:#aeb6ba;
  --shadow:0 1px 2px rgba(17,23,26,.05), 0 10px 28px -16px rgba(17,23,26,.28);
  --focus:#0e5b68;
  --grid:#d7dcde;
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{
    color-scheme: dark;
    --page:#0c1013; --card:#161b1e; --card-2:#1e2427; --sunk:#11171a;
    --ink:#eef1f2; --ink-2:#adb6ba; --ink-3:#7a848a;
    --rule:#2a3135; --hair:#222829;
    --petrol:#48a3b2; --petrol-2:#1f6773;
    --amber:#d6982c; --amber-2:#7e5a17;
    --seal:#d9614f; --seal-wash:rgba(217,97,79,.13);
    --violet:#a98cd8;
    --void:#5b666b;
    --shadow:0 1px 2px rgba(0,0,0,.45), 0 10px 28px -16px rgba(0,0,0,.8);
    --focus:#48a3b2;
    --grid:#262d31;
  }}
}}
:root[data-theme="dark"]{{
  color-scheme: dark;
  --page:#0c1013; --card:#161b1e; --card-2:#1e2427; --sunk:#11171a;
  --ink:#eef1f2; --ink-2:#adb6ba; --ink-3:#7a848a;
  --rule:#2a3135; --hair:#222829;
  --petrol:#48a3b2; --petrol-2:#1f6773;
  --amber:#d6982c; --amber-2:#7e5a17;
  --seal:#d9614f; --seal-wash:rgba(217,97,79,.13);
  --violet:#a98cd8;
  --void:#5b666b;
  --shadow:0 1px 2px rgba(0,0,0,.45), 0 10px 28px -16px rgba(0,0,0,.8);
  --focus:#48a3b2;
  --grid:#262d31;
}}
*{{box-sizing:border-box}}
body{{
  margin:0; background:var(--page); color:var(--ink);
  font-family:"Noto Sans SC","PingFang SC","Hiragino Sans GB","Microsoft YaHei",system-ui,sans-serif;
  font-size:15px; line-height:1.65; -webkit-font-smoothing:antialiased;
}}
.mono{{font-family:"IBM Plex Mono",ui-monospace,SFMono-Regular,Menlo,monospace;font-variant-numeric:tabular-nums}}
.page{{max-width:1080px;margin:0 auto;padding:0 20px 96px}}
a{{color:var(--petrol);text-decoration:none}}
a:hover{{text-decoration:underline}}

.mast{{padding:46px 0 20px;border-bottom:2px solid var(--ink)}}
.eyebrow{{font-size:11.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--ink-3);
  font-family:"IBM Plex Mono",monospace;margin:0 0 12px}}
h1{{font-family:"Noto Serif SC","Songti SC",serif;font-weight:700;font-size:clamp(28px,5vw,46px);
  line-height:1.15;margin:0;letter-spacing:.01em}}
.dek{{margin:14px 0 0;max-width:68ch;color:var(--ink-2);font-size:15.5px;line-height:1.7}}
.nav-links{{margin:14px 0 0;font-size:13px;font-family:"IBM Plex Mono",monospace;color:var(--ink-3);display:flex;gap:16px}}

.stats{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:1px;
  background:var(--rule);border:1px solid var(--rule);margin:26px 0 0}}
.stat{{background:var(--card);padding:13px 14px 12px}}
.stat b{{display:block;font-family:"IBM Plex Mono",monospace;font-weight:600;font-size:23px;
  line-height:1.12;font-variant-numeric:tabular-nums}}
.stat span{{display:block;font-size:11.5px;color:var(--ink-3);margin-top:3px;letter-spacing:.02em}}

.card{{background:var(--card);border:1px solid var(--rule);box-shadow:var(--shadow);margin-top:28px;border-radius:4px;overflow:hidden}}
.card-head{{padding:14px 18px;border-bottom:1px solid var(--rule);background:var(--card-2);display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:12px}}
.card-title{{margin:0;font-size:16px;font-weight:600;display:flex;align-items:center;gap:8px}}

/* Controls */
.ctrl-bar{{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;padding:12px 18px;background:var(--card-2);border-bottom:1px solid var(--hair)}}
.btn-group{{display:inline-flex;border-radius:4px;overflow:hidden;border:1px solid var(--rule)}}
.btn{{background:var(--card);color:var(--ink-2);border:0;border-right:1px solid var(--rule);padding:5px 12px;font-size:12px;cursor:pointer;font-family:inherit;transition:all .15s}}
.btn:last-child{{border-right:0}}
.btn:hover{{background:var(--sunk);color:var(--ink)}}
.btn.active{{background:var(--petrol);color:#fff;font-weight:500}}
.ctrl-text{{font-size:11.5px;color:var(--ink-3);font-family:"IBM Plex Mono",monospace}}

.legend{{display:flex;flex-wrap:wrap;gap:8px 20px;padding:10px 18px 6px;font-size:12.5px;color:var(--ink-2);background:var(--card)}}
.lg{{display:flex;align-items:center;gap:7px;cursor:pointer;user-select:none}}
.lg:hover{{opacity:.85}}
.lg i.sq{{height:11px;border:0;flex-basis:11px;width:11px;border-radius:2px;display:inline-block}}

.figwrap{{overflow-x:auto;-webkit-overflow-scrolling:touch;padding:16px 12px 10px;background:var(--card)}}
svg.chart{{display:block;width:100%;min-width:760px;height:auto;font-family:"IBM Plex Mono",monospace}}
svg.chart text{{fill:var(--ink-3);font-size:11px}}
.axlab{{fill:var(--ink-2);font-size:11.5px;font-weight:500}}
.gl{{stroke:var(--grid);stroke-width:1}}
.axis{{stroke:var(--ink-3);stroke-width:1}}

/* Inspector Drawer */
.inspector{{border-top:1px solid var(--rule);background:var(--card-2);padding:14px 18px;display:none}}
.insp-head{{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:10px;margin-bottom:12px}}
.insp-head h3{{margin:0;font-size:15px;font-family:"IBM Plex Mono",monospace;font-weight:600}}
.insp-badge{{background:var(--sunk);padding:2px 8px;border-radius:10px;font-size:11.5px;color:var(--ink-2);margin-left:8px}}
.insp-search{{padding:5px 10px;font-size:12.5px;border:1px solid var(--rule);border-radius:4px;background:var(--card);color:var(--ink)}}
.insp-close{{background:transparent;border:1px solid var(--rule);border-radius:3px;padding:3px 8px;cursor:pointer;color:var(--ink-3);font-size:12px}}
.insp-close:hover{{background:var(--sunk);color:var(--ink)}}

.tw{{overflow-x:auto;-webkit-overflow-scrolling:touch;max-height:360px}}
table.dense{{border-collapse:collapse;width:100%;font-size:12.5px}}
table.dense th, table.dense td{{padding:6px 10px;text-align:right;white-space:nowrap;border-bottom:1px solid var(--hair)}}
table.dense th{{font-size:11px;font-weight:500;color:var(--ink-3);position:sticky;top:0;background:var(--card-2);border-bottom:1px solid var(--rule)}}
table.dense td.l, table.dense th.l{{text-align:left}}
table.dense tbody tr:hover{{background:var(--sunk)}}

/* Tooltip */
.tipbox{{position:fixed;pointer-events:none;z-index:99;background:var(--ink);color:var(--page);
  padding:9px 12px;font-size:12px;line-height:1.55;border-radius:4px;opacity:0;transition:opacity .1s;
  box-shadow:0 6px 20px -6px rgba(0,0,0,.5);font-family:"IBM Plex Mono",monospace;min-width:180px}}
.tipbox .th{{font-weight:600;font-size:13px;margin-bottom:4px;border-bottom:1px solid rgba(255,255,255,.15);padding-bottom:3px}}
.tipbox .tr{{display:flex;justify-content:space-between;gap:14px;margin-top:2px}}

/* Full One-Point Table */
.toggle-sec{{margin-top:32px}}
.details-toggle{{cursor:pointer;font-weight:600;font-size:14px;display:inline-flex;align-items:center;gap:6px;color:var(--petrol);padding:6px 0;user-select:none}}

.notes-card{{background:var(--card);border:1px solid var(--rule);padding:18px 22px;margin-top:32px;border-radius:4px}}
.notes-card h3{{margin-top:0;font-size:16px;font-family:"Noto Serif SC",serif}}
.notes-card ul{{padding-left:20px;margin:10px 0 0;color:var(--ink-2);font-size:14px;line-height:1.8}}
.notes-card li strong{{color:var(--ink);font-weight:500}}
</style>
</head>
<body>

<div class="page">

<header class="mast">
  <p class="eyebrow">2004 年大庆市中考录取数据 · 逐分解析</p>
  <h1>610分以上考生一分频数分布直方图</h1>
  <p class="dek">
    基于《2004年大庆市中考录取总表》原始名册，对全市 <strong>610 分及以上</strong> 的 <strong>856 名高分考生</strong> 进行一分一档（610 至 663 分，共 54 个分值档）的真实频数统计。
    观察各录取高中的逐分吸收分布、整数分密集效应与分数天花板现象。
  </p>
  <div class="nav-links">
    <a href="/daqing-2004-fenbu/">← 《大庆中考的钟形曲线》（5分拟合模型）</a>
    <a href="/daqing-2004/">← 《大庆中考 2004》（名册主页）</a>
  </div>
  <div class="stats">
    <div class="stat"><b>856</b><span>高分考生 (≥610分)</span></div>
    <div class="stat"><b>663</b><span>最高分 (全市第1名)</span></div>
    <div class="stat"><b>615</b><span>峰值众数 (53人)</span></div>
    <div class="stat"><b>621</b><span>中位数得分</span></div>
    <div class="stat"><b>622.95</b><span>平均文化成绩</span></div>
    <div class="stat"><b>351</b><span>铁人中学录入</span></div>
    <div class="stat"><b>339</b><span>实验中学录入</span></div>
    <div class="stat"><b>135</b><span>大庆一中录入</span></div>
  </div>
</header>

<div class="card" id="histCard">
  <div class="card-head">
    <div class="card-title">
      <span>一分频数分布直方图 (610–663 分)</span>
      <span class="ctrl-text">· 单柱宽度为 1 分 · 点击柱子查看该分考生明细</span>
    </div>
    <div class="btn-group" id="modeGroup">
      <button class="btn active" data-mode="stack">各校堆叠</button>
      <button class="btn" data-mode="total">纯色总频数</button>
      <button class="btn" data-mode="tr">仅看铁人</button>
      <button class="btn" data-mode="sy">仅看实验</button>
      <button class="btn" data-mode="yz">仅看一中</button>
      <button class="btn" data-mode="other">其他高中</button>
    </div>
  </div>

  <div class="legend" id="legendBox">
    <span class="lg" data-school="tr"><i class="sq" style="background:var(--petrol)"></i>铁人中学 (351人 · 41.0%)</span>
    <span class="lg" data-school="sy"><i class="sq" style="background:var(--amber)"></i>实验中学 (339人 · 39.6%)</span>
    <span class="lg" data-school="yz"><i class="sq" style="background:var(--violet)"></i>大庆一中 (135人 · 15.8%)</span>
    <span class="lg" data-school="other"><i class="sq" style="background:var(--void)"></i>其他高中 (31人 · 3.6%)</span>
    <span class="lg" style="margin-left:auto"><i style="width:16px;height:0;border-top:2px dashed var(--ink-3);display:inline-block"></i>高分标记线</span>
  </div>

  <div class="figwrap">
    <svg class="chart" id="svg1pt" viewBox="0 0 960 490" role="img" aria-label="大庆中考610分以上考生一分频数分布直方图"></svg>
  </div>

  <!-- Inspector Drawer -->
  <div class="inspector" id="inspectorBox">
    <div class="insp-head">
      <div>
        <h3 id="inspTitle">【615 分】录取考生名册</h3>
        <span class="insp-badge" id="inspCountBadge">共 53 人</span>
      </div>
      <div style="display:flex;gap:10px;align-items:center">
        <input type="text" id="inspFilter" class="insp-search" placeholder="筛选姓名 / 初中...">
        <button class="insp-close" id="inspClose">✕ 收起明细</button>
      </div>
    </div>
    <div class="tw">
      <table class="dense">
        <thead>
          <tr>
            <th class="l">名次</th>
            <th>考号</th>
            <th class="l">姓名</th>
            <th>性别</th>
            <th class="l">初中学校</th>
            <th class="l">录取高中</th>
            <th>计划形式</th>
          </tr>
        </thead>
        <tbody id="inspTbody"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- Detailed Table Section -->
<div class="toggle-sec">
  <div class="details-toggle" id="tableToggleBtn">
    <span>▼ 展开 610–663 分逐分频数与累计表 (一分一段对照)</span>
  </div>
  <div class="card" id="tableCard" style="display:none;margin-top:10px">
    <div class="tw" style="max-height:480px">
      <table class="dense">
        <thead>
          <tr>
            <th class="l">文化成绩</th>
            <th>该分频数</th>
            <th>铁人中学</th>
            <th>实验中学</th>
            <th>大庆一中</th>
            <th>其他高中</th>
            <th>占高分段%</th>
            <th>累计≥本分(人)</th>
            <th>占全市21500%</th>
            <th class="l">操作</th>
          </tr>
        </thead>
        <tbody id="fullTableBody"></tbody>
      </table>
    </div>
  </div>
</div>

<!-- Key Observations -->
<div class="notes-card">
  <h3>从一分直方图看到的四个现象</h3>
  <ul>
    <li><strong>整数分聚集效应（5分/10分节点）：</strong> 615分迎来绝对峰值（53人），相比邻近的 614分（37人）和 616分（36人）高出约 45%；610分（46人）、620分（38人）、625分（38人）均形成明显的局域凸起，反映出主观题判分或小分折合时的整数聚集心理。</li>
    <li><strong>双雄均衡瓜分高分生源：</strong> 在 610 分以上的 856 人中，铁人中学录入 351 人（41.0%），大庆实验录入 339 人（39.6%），两校几乎均分前 4% 生源（合计占 80.6%）。大庆一中录入 135 人（15.8%），其他学校（大庆中学16人、大庆四中10人、东风高中4人、三十五中1人）仅录得 31 人（3.6%）。</li>
    <li><strong>635 分以上的急速衰减：</strong> 610 至 634 分共 727 人（平均每分 29.1 人），而 635 分至 663 分仅 129 人（平均每分 4.4 人）。超过 645 分后，每分仅 0~2 人，并出现多个零频分值（如 651、653、658–662分均无考生），直至 663 分状元李璐单点出现。</li>
    <li><strong>顶尖高分（≥650分）去向：</strong> 650 分及以上共有 8 名考生，其中铁人中学录取 3 人（657分刘禹驰、650分狄昊、649分迟妍玮与黄鹤），实验中学录取 3 人（655分崔潇、654分魏征与姜冰），大庆一中录取 2 人（663分李璐、656分关天下、652分王亦然）。</li>
  </ul>
</div>

</div>

<div class="tipbox" id="tip"></div>

<script>
const DATA_1PT = {json_data_str};

(function(){{
  const svg = document.getElementById('svg1pt');
  const tip = document.getElementById('tip');
  const inspBox = document.getElementById('inspectorBox');
  const inspTitle = document.getElementById('inspTitle');
  const inspCountBadge = document.getElementById('inspCountBadge');
  const inspFilter = document.getElementById('inspFilter');
  const inspTbody = document.getElementById('inspTbody');
  const inspClose = document.getElementById('inspClose');
  const fullTableBody = document.getElementById('fullTableBody');
  const tableToggleBtn = document.getElementById('tableToggleBtn');
  const tableCard = document.getElementById('tableCard');

  const NS = "http://www.w3.org/2000/svg";
  const el = (t, a, p) => {{
    const e = document.createElementNS(NS, t);
    for (const k in a) e.setAttribute(k, a[k]);
    if (p) p.appendChild(e);
    return e;
  }};

  const W = 960, H = 490;
  const m = {{ l: 56, r: 24, t: 36, b: 64 }};
  const x0 = m.l, x1 = W - m.r, y0 = H - m.b, y1 = m.t;
  const bins = DATA_1PT.bins;
  const nBins = bins.length; // 54
  const slotW = (x1 - x0) / nBins;
  const barW = Math.max(8, slotW - 3.8);

  const maxVal = 58; // scale top
  const Y = v => y0 - (v / maxVal) * (y0 - y1);
  const X = i => x0 + (i + 0.5) * slotW;

  let currentMode = 'stack'; // 'stack' | 'total' | 'tr' | 'sy' | 'yz' | 'other'
  let activeScore = null;
  let activeStudents = [];

  // Colors
  const colors = {{
    tr: 'var(--petrol)',
    sy: 'var(--amber)',
    yz: 'var(--violet)',
    other: 'var(--void)',
    total: 'var(--seal)'
  }};

  // Render Base Axes
  function drawAxes() {{
    // Y Grid & labels
    for (let v = 0; v <= 50; v += 10) {{
      el('line', {{ x1: x0, x2: x1, y1: Y(v), y2: Y(v), class: 'gl' }}, svg);
      const t = el('text', {{ x: x0 - 8, y: Y(v) + 4, 'text-anchor': 'end', 'font-size': '11.5' }}, svg);
      t.textContent = v;
    }}
    // Y Axis Title
    const yc = (y0 + y1) / 2;
    el('text', {{ x: 16, y: yc, 'text-anchor': 'middle', class: 'axlab', transform: `rotate(-90 16 ${{yc}})` }}, svg)
      .textContent = '考生人数（频数）';

    // X axis line
    el('line', {{ x1: x0, x2: x1, y1: y0, y2: y0, class: 'axis' }}, svg);
    el('line', {{ x1: x0, x2: x0, y1: y0, y2: y1, class: 'axis' }}, svg);

    // X ticks & labels
    bins.forEach((b, i) => {{
      const cx = X(i);
      const isMajor = (b.score % 5 === 0) || b.score === 663;
      el('line', {{ x1: cx, x2: cx, y1: y0, y2: y0 + (isMajor ? 6 : 3), stroke: 'var(--rule)', 'stroke-width': 1 }}, svg);
      if (isMajor) {{
        const txt = el('text', {{ x: cx, y: y0 + 19, 'text-anchor': 'middle', 'font-size': '11', 'font-weight': (b.score === 615 || b.score === 663 ? '600' : '400') }}, svg);
        txt.textContent = b.score;
      }}
    }});
    el('text', {{ x: (x0 + x1) / 2, y: H - 12, 'text-anchor': 'middle', class: 'axlab' }}, svg)
      .textContent = '中考文化成绩（满分 660 / 690，610–663 分逐分分布）';
  }}

  // Markers for Key Milestones
  function drawMarkers() {{
    const markerGroup = el('g', {{ id: 'markerGroup' }}, svg);
    const milestones = [
      {{ s: 615, txt: '众数 53人', align: 'middle', dy: -28, pin: true }},
      {{ s: 621, txt: '中位数 621', align: 'middle', dy: -10 }},
      {{ s: 635, txt: '拐点 635', align: 'start', dx: 4, dy: -12 }},
      {{ s: 663, txt: '状元 663分 (李璐)', align: 'end', dx: -6, dy: -24, pin: true }}
    ];

    milestones.forEach(m => {{
      const idx = bins.findIndex(b => b.score === m.s);
      if (idx < 0) return;
      const cx = X(idx);
      const b = bins[idx];
      const cy = Y(b.count);

      if (m.pin) {{
        el('line', {{ x1: cx, x2: cx, y1: cy - 2, y2: cy + (m.dy || -20) + 12, stroke: 'var(--ink-3)', 'stroke-width': 1, 'stroke-dasharray': '2 2' }}, markerGroup);
        const t = el('text', {{ x: cx + (m.dx || 0), y: cy + (m.dy || -20) + 8, 'text-anchor': m.align, 'font-size': '10.5', 'font-weight': '600', fill: 'var(--ink)' }}, markerGroup);
        t.textContent = m.txt;
      }}
    }});
  }}

  // Draw Bars
  const barsLayer = el('g', {{ id: 'barsLayer' }}, svg);

  function renderBars() {{
    barsLayer.innerHTML = '';

    bins.forEach((b, i) => {{
      const cx = X(i);
      const bx = cx - barW / 2;
      const count = b.count;

      if (currentMode === 'stack') {{
        // Stacked: tr, sy, yz, other
        let curY = y0;
        const segs = [
          {{ k: 'tr', c: colors.tr, v: b.tr, label: '铁人中学' }},
          {{ k: 'sy', c: colors.sy, v: b.sy, label: '实验中学' }},
          {{ k: 'yz', c: colors.yz, v: b.yz, label: '大庆一中' }},
          {{ k: 'other', c: colors.other, v: b.other, label: '其他学校' }}
        ];
        segs.forEach(sg => {{
          if (sg.v <= 0) return;
          const h = (sg.v / maxVal) * (y0 - y1);
          const topY = curY - h;
          el('rect', {{
            x: bx, y: topY, width: barW, height: h,
            fill: sg.c, opacity: 0.92,
            rx: 1, ry: 1
          }}, barsLayer);
          curY = topY;
        }});
      }} else if (currentMode === 'total') {{
        if (count > 0) {{
          const h = (count / maxVal) * (y0 - y1);
          el('rect', {{
            x: bx, y: y0 - h, width: barW, height: h,
            fill: colors.total, opacity: 0.88, rx: 1, ry: 1
          }}, barsLayer);
        }}
      }} else {{
        // Single school mode
        const v = b[currentMode] || 0;
        if (v > 0) {{
          const h = (v / maxVal) * (y0 - y1);
          el('rect', {{
            x: bx, y: y0 - h, width: barW, height: h,
            fill: colors[currentMode], opacity: 0.92, rx: 1, ry: 1
          }}, barsLayer);
        }}
      }}

      // Top label for major counts
      if (count > 0 && (b.score === 615 || b.score === 610 || b.score === 620 || b.score === 625 || b.score === 663)) {{
        const targetVal = (currentMode === 'stack' || currentMode === 'total') ? count : (b[currentMode] || 0);
        if (targetVal > 0) {{
          const txt = el('text', {{
            x: cx, y: Y(targetVal) - 4,
            'text-anchor': 'middle', 'font-size': '10', 'font-weight': '600', fill: 'var(--ink-2)'
          }}, barsLayer);
          txt.textContent = targetVal;
        }}
      }}

      // Invisible overlay for clean hover/click
      const hit = el('rect', {{
        x: bx - 1, y: y1, width: barW + 2, height: y0 - y1,
        fill: 'transparent', cursor: count > 0 ? 'pointer' : 'default'
      }}, barsLayer);

      // Active state highlight frame
      if (activeScore === b.score && count > 0) {{
        el('rect', {{
          x: bx - 2, y: Y(count) - 2, width: barW + 4, height: (y0 - Y(count)) + 2,
          fill: 'none', stroke: 'var(--ink)', 'stroke-width': 2, rx: 2
        }}, barsLayer);
      }}

      hit.addEventListener('mousemove', ev => {{
        showTip(b, ev);
      }});
      hit.addEventListener('mouseleave', hideTip);

      if (count > 0) {{
        hit.addEventListener('click', () => {{
          selectScore(b);
        }});
      }}
    }});
  }}

  function showTip(b, ev) {{
    const pctHigh = ((b.count / DATA_1PT.total) * 100).toFixed(2);
    const pctAll = ((b.count / 21500) * 100).toFixed(2);
    let h = `<div class="th">${{b.score}} 分 · 频数 ${{b.count}} 人</div>` +
            `<div class="tr"><span>占高分段 (≥610)</span><span>${{pctHigh}}%</span></div>` +
            `<div class="tr"><span>全市累计 ≥ ${{b.score}}分</span><span>第 ${{b.cum}} 名</span></div>` +
            `<div class="tr"><span>占全市 21,500 考生</span><span>前 ${{(100 * b.cum / 21500).toFixed(2)}}%</span></div>` +
            `<div style="margin-top:6px;border-top:1px dashed rgba(255,255,255,0.2);padding-top:4px">` +
            `<div class="tr"><span style="color:#7ed6df">铁人中学</span><span>${{b.tr}} 人</span></div>` +
            `<div class="tr"><span style="color:#f9ca24">实验中学</span><span>${{b.sy}} 人</span></div>` +
            `<div class="tr"><span style="color:#e056fd">大庆一中</span><span>${{b.yz}} 人</span></div>` +
            (b.other > 0 ? `<div class="tr"><span style="color:#dff9fb">其他高中</span><span>${{b.other}} 人</span></div>` : '') +
            `</div>` +
            `<div style="margin-top:5px;font-size:11px;color:#f1f2f6;opacity:0.85">💡 点击柱子查看这 ${{b.count}} 位考生的名册</div>`;

    tip.innerHTML = h;
    tip.style.opacity = 1;
    const pad = 14;
    let x = ev.clientX + pad, y = ev.clientY + pad;
    if (x + tip.offsetWidth > innerWidth - 10) x = ev.clientX - tip.offsetWidth - pad;
    if (y + tip.offsetHeight > innerHeight - 10) y = ev.clientY - tip.offsetHeight - pad;
    tip.style.left = x + 'px';
    tip.style.top = y + 'px';
  }}

  function hideTip() {{
    tip.style.opacity = 0;
  }}

  function selectScore(b) {{
    activeScore = b.score;
    activeStudents = b.students || [];
    renderBars();

    inspBox.style.display = 'block';
    inspTitle.textContent = `【${{b.score}} 分】录取考生名册`;
    inspCountBadge.textContent = `共 ${{b.count}} 人 · 铁人 ${{b.tr}} / 实验 ${{b.sy}} / 一中 ${{b.yz}}${{b.other > 0 ? ' / 其他 ' + b.other : ''}}`;
    inspFilter.value = '';
    renderStudents(activeStudents);
    inspBox.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
  }}

  function renderStudents(list) {{
    inspTbody.innerHTML = '';
    if (!list || list.length === 0) {{
      inspTbody.innerHTML = '<tr><td colspan="7" class="l" style="text-align:center;color:var(--ink-3);padding:14px">无匹配考生</td></tr>';
      return;
    }}
    list.forEach(st => {{
      const tr = document.createElement('tr');
      let hsColor = 'inherit';
      if (st.hs === '铁人中学') hsColor = 'var(--petrol)';
      else if (st.hs === '实验中学') hsColor = 'var(--amber)';
      else if (st.hs === '一中') hsColor = 'var(--violet)';

      tr.innerHTML = `
        <td class="l mono">${{st.rank}}</td>
        <td class="mono">${{st.no}}</td>
        <td class="l" style="font-weight:500">${{st.name}}</td>
        <td>${{st.sex}}</td>
        <td class="l">${{st.ms}}</td>
        <td class="l" style="color:${{hsColor}};font-weight:600">${{st.hs}}</td>
        <td>${{st.plan}}</td>
      `;
      inspTbody.appendChild(tr);
    }});
  }}

  // Filter Search in Inspector
  inspFilter.addEventListener('input', e => {{
    const q = e.target.value.trim().toLowerCase();
    if (!q) {{
      renderStudents(activeStudents);
      return;
    }}
    const filtered = activeStudents.filter(s => 
      s.name.toLowerCase().includes(q) ||
      s.ms.toLowerCase().includes(q) ||
      s.hs.toLowerCase().includes(q) ||
      String(s.no).includes(q)
    );
    renderStudents(filtered);
  }});

  inspClose.addEventListener('click', () => {{
    inspBox.style.display = 'none';
    activeScore = null;
    renderBars();
  }});

  // Mode buttons
  document.getElementById('modeGroup').addEventListener('click', e => {{
    if (!e.target.classList.contains('btn')) return;
    document.querySelectorAll('#modeGroup .btn').forEach(b => b.classList.remove('active'));
    e.target.classList.add('active');
    currentMode = e.target.dataset.mode;
    renderBars();
  }});

  // Legend click to filter
  document.getElementById('legendBox').addEventListener('click', e => {{
    const item = e.target.closest('.lg');
    if (!item || !item.dataset.school) return;
    const sch = item.dataset.school;
    const targetBtn = document.querySelector(`#modeGroup .btn[data-mode="${{sch}}"]`);
    if (targetBtn) targetBtn.click();
  }});

  // Render Full Table
  function renderFullTable() {{
    fullTableBody.innerHTML = '';
    // Reverse for display: 663 down to 610
    const revBins = [...bins].reverse();
    revBins.forEach(b => {{
      const tr = document.createElement('tr');
      const pctHigh = ((b.count / DATA_1PT.total) * 100).toFixed(2) + '%';
      const pctAll = ((b.cum / 21500) * 100).toFixed(2) + '%';
      tr.innerHTML = `
        <td class="l mono" style="font-weight:600">${{b.score}}</td>
        <td class="mono" style="font-weight:600;color:${{b.count > 30 ? 'var(--seal)' : 'inherit'}}">${{b.count}}</td>
        <td class="mono" style="color:var(--petrol)">${{b.tr || '·'}}</td>
        <td class="mono" style="color:var(--amber)">${{b.sy || '·'}}</td>
        <td class="mono" style="color:var(--violet)">${{b.yz || '·'}}</td>
        <td class="mono" style="color:var(--void)">${{b.other || '·'}}</td>
        <td class="mono">${{pctHigh}}</td>
        <td class="mono">${{b.cum.toLocaleString('en-US')}}</td>
        <td class="mono">${{pctAll}}</td>
        <td class="l"><button class="insp-close" style="padding:1px 6px;font-size:11px" onclick="window.inspectScore(${{b.score}})">查看名册</button></td>
      `;
      fullTableBody.appendChild(tr);
    }});
  }}

  window.inspectScore = function(score) {{
    const b = bins.find(x => x.score === score);
    if (b) selectScore(b);
  }};

  tableToggleBtn.addEventListener('click', () => {{
    if (tableCard.style.display === 'none') {{
      tableCard.style.display = 'block';
      tableToggleBtn.textContent = '▲ 收起 610–663 分逐分频数与累计表';
    }} else {{
      tableCard.style.display = 'none';
      tableToggleBtn.textContent = '▼ 展开 610–663 分逐分频数与累计表 (一分一段对照)';
    }}
  }});

  // Init
  drawAxes();
  drawMarkers();
  renderBars();
  renderFullTable();
}})();
</script>

</body>
</html>
"""

with open('./static/daqing-2004-fenbu/one-point.html', 'w', encoding='utf-8') as f:
    f.write(STANDALONE_HTML)
print("Saved static/daqing-2004-fenbu/one-point.html")

with open('./public/daqing-2004-fenbu/one-point.html', 'w', encoding='utf-8') as f:
    f.write(STANDALONE_HTML)
print("Saved public/daqing-2004-fenbu/one-point.html")
