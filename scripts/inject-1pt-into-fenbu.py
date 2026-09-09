#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Inject the 1-point frequency distribution histogram section into static/daqing-2004-fenbu/index.html
and sync to public/daqing-2004-fenbu/index.html
"""

import json
import re
import shutil
import pandas as pd

CSV_PATH = './public/2004/2004年大庆中考录取总表.csv'
df = pd.read_csv(CSV_PATH)

high = df[df['文化成绩'] >= 610].sort_values(by=['文化成绩', '名次'], ascending=[False, True])

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

bins_asc = sorted(bins_1pt, key=lambda x: x['score'])

DATA_1PT = {
    'total': len(high),
    'mean': round(float(high['文化成绩'].mean()), 2),
    'median': float(high['文化成绩'].median()),
    'std': round(float(high['文化成绩'].std()), 2),
    'mode': int(high['文化成绩'].mode()[0]),
    'modeCount': int((high['文化成绩'] == int(high['文化成绩'].mode()[0])).sum()),
    'max': int(high['文化成绩'].max()),
    'min': int(high['文化成绩'].min()),
    'bins': bins_asc
}

json_str = json.dumps(DATA_1PT, ensure_ascii=False, separators=(',', ':'))

with open('static/daqing-2004-fenbu/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add link in masthead back nav
old_back = '<p class="back">← <a href="/daqing-2004/">《大庆中考 2004》</a>　·　姊妹页</p>'
new_back = ('<p class="back">← <a href="/daqing-2004/">《大庆中考 2004》</a>　·　'
            '<a href="#hist1pt" style="color:var(--seal);font-weight:600">📊 直达一分频数直方图 (856人)</a>　·　'
            '<a href="/daqing-2004-fenbu/one-point.html" target="_blank" style="color:var(--petrol)">↗ 独立全屏视图</a></p>')
if old_back in html:
    html = html.replace(old_back, new_back)

# 2. Add extra CSS
extra_css = """
/* 1-point Histogram Styles */
.ctrl-bar{display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;padding:10px 16px;background:var(--card-2);border-bottom:1px solid var(--hair)}
.btn-group{display:inline-flex;border-radius:4px;overflow:hidden;border:1px solid var(--rule)}
.btn{background:var(--card);color:var(--ink-2);border:0;border-right:1px solid var(--rule);padding:4px 11px;font-size:11.5px;cursor:pointer;font-family:inherit;transition:all .15s}
.btn:last-child{border-right:0}
.btn:hover{background:var(--sunk);color:var(--ink)}
.btn.active{background:var(--petrol);color:#fff;font-weight:500}
.ctrl-text{font-size:11.5px;color:var(--ink-3);font-family:"IBM Plex Mono",monospace}
.inspector{border-top:1px solid var(--rule);background:var(--card-2);padding:14px 18px;display:none}
.insp-head{display:flex;flex-wrap:wrap;align-items:baseline;justify-content:space-between;gap:10px;margin-bottom:10px}
.insp-head h3{margin:0;font-size:14px;font-family:"IBM Plex Mono",monospace;font-weight:600}
.insp-badge{background:var(--sunk);padding:2px 7px;border-radius:10px;font-size:11px;color:var(--ink-2);margin-left:6px}
.insp-search{padding:4px 8px;font-size:12px;border:1px solid var(--rule);border-radius:3px;background:var(--card);color:var(--ink)}
.insp-close{background:transparent;border:1px solid var(--rule);border-radius:3px;padding:2px 7px;cursor:pointer;color:var(--ink-3);font-size:11.5px}
.insp-close:hover{background:var(--sunk);color:var(--ink)}
table.dense{border-collapse:collapse;width:100%;font-size:12px}
table.dense th, table.dense td{padding:5px 8px;text-align:right;white-space:nowrap;border-bottom:1px solid var(--hair)}
table.dense th{font-size:11px;font-weight:500;color:var(--ink-3);position:sticky;top:0;background:var(--card-2);border-bottom:1px solid var(--rule)}
table.dense td.l, table.dense th.l{text-align:left}
table.dense tbody tr:hover{background:var(--sunk)}
</style>
"""

if '</style>' in html and '.ctrl-bar' not in html:
    html = html.replace('</style>', extra_css)

# 3. Add section #hist1pt right before <section id="hist">
section_html = """
<section id="hist1pt">
  <div class="sechead"><h2>一分频数分布直方图（610–663 分逐分实测）</h2><span class="tag">856 人 · 逐分分布</span></div>
  <p class="lede">
    根据《2004年大庆市中考录取总表》，<strong>610 分及以上共有 856 名考生</strong>（占全市 21500 考生的前 3.98%）。
    不同于宏观 5 分一组的拟合，这里以 <strong>1 分为组距</strong> 绘制绝对真实的频数柱状图（共 54 个分值档）。
    每根柱子直接反映各高中的实际生源瓜分；<strong>点击柱子可直接展开该分数的考生录用名册</strong>。
  </p>
  <div class="card fig" style="border-radius:4px;overflow:hidden">
    <div class="ctrl-bar">
      <div class="btn-group" id="btnGroup1pt">
        <button class="btn active" data-mode="stack">各校堆叠频数</button>
        <button class="btn" data-mode="total">纯色总频数</button>
        <button class="btn" data-mode="tr">铁人中学 (351人)</button>
        <button class="btn" data-mode="sy">实验中学 (339人)</button>
        <button class="btn" data-mode="yz">大庆一中 (135人)</button>
        <button class="btn" data-mode="other">其他高中 (31人)</button>
      </div>
      <span class="ctrl-text" style="margin-left:auto">单柱宽度 1 分 · 峰值 615分 (53人) · 最高 663分</span>
    </div>
    <div class="legend" id="legend1pt">
      <span class="lg"><i class="sq" style="background:var(--petrol)"></i>铁人中学 (351人 · 41.0%)</span>
      <span class="lg"><i class="sq" style="background:var(--amber)"></i>实验中学 (339人 · 39.6%)</span>
      <span class="lg"><i class="sq" style="background:var(--violet)"></i>大庆一中 (135人 · 15.8%)</span>
      <span class="lg"><i class="sq" style="background:var(--void)"></i>其他学校 (31人 · 3.6%)</span>
      <a href="/daqing-2004-fenbu/one-point.html" target="_blank" style="margin-left:auto;font-size:12px;font-family:'IBM Plex Mono',monospace">↗ 打开独立全屏交互版</a>
    </div>
    <div class="figwrap">
      <svg class="chart" id="chart1pt" viewBox="0 0 960 480" role="img" aria-label="大庆中考610分以上考生一分频数分布直方图"></svg>
    </div>
    <figcaption>
      <b>一分直方图启示：</b>
      ① <b>615 分迎来绝对峰值（53 人）</b>，且 610、620、625 分均有显著的“逢五逢十”整数分聚集效应；
      ② 铁人中学与大庆实验在高分段平分秋色（41.0% vs 39.6%），大庆一中录得 15.8%；
      ③ <b>635 分</b>后人数陡降，645 分以上极为稀薄，650+ 仅 8 人，状元李璐以 663 分单点领先。
    </figcaption>

    <!-- Inspector Drawer -->
    <div class="inspector" id="drawer1pt">
      <div class="insp-head">
        <div>
          <h3 id="drawerTitle">【615 分】录取考生名册</h3>
          <span class="insp-badge" id="drawerBadge">共 53 人</span>
        </div>
        <div style="display:flex;gap:10px;align-items:center">
          <input type="text" id="drawerSearch" class="insp-search" placeholder="筛选姓名 / 初中学校...">
          <button class="insp-close" id="drawerClose">✕ 收起</button>
        </div>
      </div>
      <div class="tw" style="max-height:320px">
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
          <tbody id="drawerTbody"></tbody>
        </table>
      </div>
    </div>
  </div>
</section>
"""

if '<section id="hist1pt">' not in html and '<section id="hist">' in html:
    html = html.replace('<section id="hist">', section_html + '\n<section id="hist">')

# 4. Add JS logic right before closing </script>
js_code = f"""
/* ---------- 1-Point Frequency Histogram Implementation ---------- */
const DATA_1PT = {json_str};

(function(){{
  const svg = document.getElementById('chart1pt');
  if(!svg) return;
  const tip = document.getElementById('tip');
  const drawer = document.getElementById('drawer1pt');
  const drawerTitle = document.getElementById('drawerTitle');
  const drawerBadge = document.getElementById('drawerBadge');
  const drawerSearch = document.getElementById('drawerSearch');
  const drawerTbody = document.getElementById('drawerTbody');
  const drawerClose = document.getElementById('drawerClose');

  const NS = "http://www.w3.org/2000/svg";
  const el = (t, a, p) => {{
    const e = document.createElementNS(NS, t);
    for (const k in a) e.setAttribute(k, a[k]);
    if (p) p.appendChild(e);
    return e;
  }};

  const W = 960, H = 480;
  const m = {{ l: 56, r: 24, t: 34, b: 62 }};
  const x0 = m.l, x1 = W - m.r, y0 = H - m.b, y1 = m.t;
  const bins = DATA_1PT.bins;
  const nBins = bins.length;
  const slotW = (x1 - x0) / nBins;
  const barW = Math.max(8, slotW - 3.8);

  const maxVal = 58;
  const Y = v => y0 - (v / maxVal) * (y0 - y1);
  const X = i => x0 + (i + 0.5) * slotW;

  let currentMode = 'stack';
  let activeScore = null;
  let activeStudents = [];

  const colors = {{
    tr: 'var(--petrol)',
    sy: 'var(--amber)',
    yz: 'var(--violet)',
    other: 'var(--void)',
    total: 'var(--seal)'
  }};

  // Axes
  for (let v = 0; v <= 50; v += 10) {{
    el('line', {{ x1: x0, x2: x1, y1: Y(v), y2: Y(v), class: 'gl' }}, svg);
    const t = el('text', {{ x: x0 - 8, y: Y(v) + 4, 'text-anchor': 'end', 'font-size': '11' }}, svg);
    t.textContent = v;
  }}
  const yc = (y0 + y1) / 2;
  el('text', {{ x: 16, y: yc, 'text-anchor': 'middle', class: 'axlab', transform: `rotate(-90 16 ${{yc}})` }}, svg)
    .textContent = '考生人数（频数）';

  el('line', {{ x1: x0, x2: x1, y1: y0, y2: y0, class: 'axis' }}, svg);
  el('line', {{ x1: x0, x2: x0, y1: y0, y2: y1, class: 'axis' }}, svg);

  bins.forEach((b, i) => {{
    const cx = X(i);
    const isMajor = (b.score % 5 === 0) || b.score === 663;
    el('line', {{ x1: cx, x2: cx, y1: y0, y2: y0 + (isMajor ? 6 : 3), stroke: 'var(--rule)', 'stroke-width': 1 }}, svg);
    if (isMajor) {{
      const txt = el('text', {{ x: cx, y: y0 + 18, 'text-anchor': 'middle', 'font-size': '11', 'font-weight': (b.score === 615 || b.score === 663 ? '600' : '400') }}, svg);
      txt.textContent = b.score;
    }}
  }});
  el('text', {{ x: (x0 + x1) / 2, y: H - 12, 'text-anchor': 'middle', class: 'axlab' }}, svg)
    .textContent = '中考文化成绩（610–663 分逐分分布）';

  // Key Milestones Pin
  const milestones = [
    {{ s: 615, txt: '众数 53人', align: 'middle', dy: -28 }},
    {{ s: 621, txt: '中位数 621', align: 'middle', dy: -10 }},
    {{ s: 635, txt: '拐点 635', align: 'start', dx: 3, dy: -12 }},
    {{ s: 663, txt: '状元 663分', align: 'end', dx: -6, dy: -22 }}
  ];
  milestones.forEach(mItem => {{
    const idx = bins.findIndex(b => b.score === mItem.s);
    if (idx < 0) return;
    const cx = X(idx);
    const b = bins[idx];
    const cy = Y(b.count);
    el('line', {{ x1: cx, x2: cx, y1: cy - 2, y2: cy + (mItem.dy || -20) + 12, stroke: 'var(--ink-3)', 'stroke-width': 1, 'stroke-dasharray': '2 2' }}, svg);
    const t = el('text', {{ x: cx + (mItem.dx || 0), y: cy + (mItem.dy || -20) + 8, 'text-anchor': mItem.align, 'font-size': '10.5', 'font-weight': '600', fill: 'var(--ink)' }}, svg);
    t.textContent = mItem.txt;
  }});

  const barsLayer = el('g', {{ id: 'barsLayer1pt' }}, svg);

  function renderBars() {{
    barsLayer.innerHTML = '';
    bins.forEach((b, i) => {{
      const cx = X(i);
      const bx = cx - barW / 2;
      const count = b.count;

      if (currentMode === 'stack') {{
        let curY = y0;
        const segs = [
          {{ k: 'tr', c: colors.tr, v: b.tr }},
          {{ k: 'sy', c: colors.sy, v: b.sy }},
          {{ k: 'yz', c: colors.yz, v: b.yz }},
          {{ k: 'other', c: colors.other, v: b.other }}
        ];
        segs.forEach(sg => {{
          if (sg.v <= 0) return;
          const h = (sg.v / maxVal) * (y0 - y1);
          const topY = curY - h;
          el('rect', {{ x: bx, y: topY, width: barW, height: h, fill: sg.c, opacity: 0.92, rx: 1, ry: 1 }}, barsLayer);
          curY = topY;
        }});
      }} else if (currentMode === 'total') {{
        if (count > 0) {{
          const h = (count / maxVal) * (y0 - y1);
          el('rect', {{ x: bx, y: y0 - h, width: barW, height: h, fill: colors.total, opacity: 0.88, rx: 1, ry: 1 }}, barsLayer);
        }}
      }} else {{
        const v = b[currentMode] || 0;
        if (v > 0) {{
          const h = (v / maxVal) * (y0 - y1);
          el('rect', {{ x: bx, y: y0 - h, width: barW, height: h, fill: colors[currentMode], opacity: 0.92, rx: 1, ry: 1 }}, barsLayer);
        }}
      }}

      // Value label on peak bars
      if (count > 0 && (b.score === 615 || b.score === 610 || b.score === 620 || b.score === 625 || b.score === 663)) {{
        const val = (currentMode === 'stack' || currentMode === 'total') ? count : (b[currentMode] || 0);
        if (val > 0) {{
          const txt = el('text', {{ x: cx, y: Y(val) - 4, 'text-anchor': 'middle', 'font-size': '10', 'font-weight': '600', fill: 'var(--ink-2)' }}, barsLayer);
          txt.textContent = val;
        }}
      }}

      // Hit area
      const hit = el('rect', {{ x: bx - 1, y: y1, width: barW + 2, height: y0 - y1, fill: 'transparent', cursor: count > 0 ? 'pointer' : 'default' }}, barsLayer);

      if (activeScore === b.score && count > 0) {{
        el('rect', {{ x: bx - 2, y: Y(count) - 2, width: barW + 4, height: (y0 - Y(count)) + 2, fill: 'none', stroke: 'var(--ink)', 'stroke-width': 2, rx: 2 }}, barsLayer);
      }}

      hit.addEventListener('mousemove', ev => {{
        const pctHigh = ((b.count / DATA_1PT.total) * 100).toFixed(2);
        let h = `<div class="th">${{b.score}} 分 · 频数 ${{b.count}} 人</div>` +
                `<div class="tr"><span>占高分段 (≥610)</span><span>${{pctHigh}}%</span></div>` +
                `<div class="tr"><span>全市累计 ≥ ${{b.score}}分</span><span>第 ${{b.cum}} 名</span></div>` +
                `<div style="margin-top:5px;border-top:1px dashed rgba(255,255,255,0.2);padding-top:3px">` +
                `<div class="tr"><span style="color:#7ed6df">铁人中学</span><span>${{b.tr}} 人</span></div>` +
                `<div class="tr"><span style="color:#f9ca24">实验中学</span><span>${{b.sy}} 人</span></div>` +
                `<div class="tr"><span style="color:#e056fd">大庆一中</span><span>${{b.yz}} 人</span></div>` +
                (b.other > 0 ? `<div class="tr"><span style="color:#dff9fb">其他高中</span><span>${{b.other}} 人</span></div>` : '') +
                `</div>` +
                `<div style="margin-top:4px;font-size:11px;color:#f1f2f6;opacity:0.85">💡 点击柱子查看考生名册</div>`;
        tip.innerHTML = h;
        tip.style.opacity = 1;
        const pad = 14;
        let x = ev.clientX + pad, y = ev.clientY + pad;
        if (x + tip.offsetWidth > innerWidth - 10) x = ev.clientX - tip.offsetWidth - pad;
        if (y + tip.offsetHeight > innerHeight - 10) y = ev.clientY - tip.offsetHeight - pad;
        tip.style.left = x + 'px'; tip.style.top = y + 'px';
      }});
      hit.addEventListener('mouseleave', () => {{ tip.style.opacity = 0; }});

      if (count > 0) {{
        hit.addEventListener('click', () => {{
          activeScore = b.score;
          activeStudents = b.students || [];
          renderBars();

          drawer.style.display = 'block';
          drawerTitle.textContent = `【${{b.score}} 分】录取考生名册`;
          drawerBadge.textContent = `共 ${{b.count}} 人 · 铁人 ${{b.tr}} / 实验 ${{b.sy}} / 一中 ${{b.yz}}${{b.other > 0 ? ' / 其他 ' + b.other : ''}}`;
          drawerSearch.value = '';
          renderDrawerList(activeStudents);
          drawer.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }});
      }}
    }});
  }}

  function renderDrawerList(list) {{
    drawerTbody.innerHTML = '';
    if (!list || list.length === 0) {{
      drawerTbody.innerHTML = '<tr><td colspan="7" class="l" style="text-align:center;color:var(--ink-3);padding:12px">无匹配考生</td></tr>';
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
      drawerTbody.appendChild(tr);
    }});
  }}

  drawerSearch.addEventListener('input', e => {{
    const q = e.target.value.trim().toLowerCase();
    if (!q) {{ renderDrawerList(activeStudents); return; }}
    const filtered = activeStudents.filter(s => 
      s.name.toLowerCase().includes(q) ||
      s.ms.toLowerCase().includes(q) ||
      s.hs.toLowerCase().includes(q) ||
      String(s.no).includes(q)
    );
    renderDrawerList(filtered);
  }});

  drawerClose.addEventListener('click', () => {{
    drawer.style.display = 'none';
    activeScore = null;
    renderBars();
  }});

  document.getElementById('btnGroup1pt').addEventListener('click', e => {{
    if (!e.target.classList.contains('btn')) return;
    document.querySelectorAll('#btnGroup1pt .btn').forEach(b => b.classList.remove('active'));
    e.target.classList.add('active');
    currentMode = e.target.dataset.mode;
    renderBars();
  }});

  renderBars();
}})();
"""

if '/* ---------- 1-Point Frequency Histogram Implementation ---------- */' not in html:
    html = html.replace('</script>', js_code + '\n</script>')

with open('static/daqing-2004-fenbu/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated static/daqing-2004-fenbu/index.html successfully")

with open('public/daqing-2004-fenbu/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated public/daqing-2004-fenbu/index.html successfully")
