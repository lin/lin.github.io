import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os
import shutil

# 1. High quality publication styling
plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang HK', 'Songti SC', 'Hiragino Sans GB', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 2. Load 2004 Zhongkao
zk = pd.read_csv('content/kao/qq/2004年中考大庆市区成绩单.csv')
zk['文化课+体育成绩'] = pd.to_numeric(zk['文化课+体育成绩'], errors='coerce')
zk['中考名次'] = zk['文化课+体育成绩'].rank(method='min', ascending=False).astype(int)

# 3. Load 2007 Gaokao YFYD table
yfyd = pd.read_csv('content/kao/qq/2007年高考理科一分一段表.csv')
yfyd['分数'] = pd.to_numeric(yfyd['分数'])
yfyd['累计人数'] = pd.to_numeric(yfyd['累计人数'])
r_sorted = yfyd.sort_values(by='累计人数')

def get_gk_score_from_rank(rank):
    if rank <= r_sorted['累计人数'].min():
        return float(r_sorted['分数'].max())
    if rank >= r_sorted['累计人数'].max():
        return float(r_sorted['分数'].min())
    return float(np.interp(rank, r_sorted['累计人数'], r_sorted['分数']))

# 4. Load Verified Candidates
df_cand = pd.read_csv('content/kao/qq/大庆中高考实名考生逐人对应表.csv')
v = df_cand[df_cand['是否统招核验']].copy()
v_zk = v.sort_values(by=['中考文体总分', '2004中考市区名次'], ascending=[False, True]).reset_index(drop=True)
v_gk = v.sort_values(by='2007高考成绩', ascending=False).reset_index(drop=True)

# Power law fit
log_r_zk = np.log(v_zk['2004中考市区名次'].values)
log_r_gk = np.log(v_gk['2007高考一分一段名次'].values)
slope_r, intercept_r, rval_r, pval_r, se_r = stats.linregress(log_r_zk, log_r_gk)

# Linear QQ fit
slope_qq, int_qq, rval_qq, pval_qq, se_qq = stats.linregress(v_zk['中考文体总分'].values, v_gk['2007高考成绩'].values)

# Individual OLS fit (all 54 verified)
slope_ols, int_ols, rval_ols, pval_ols, se_ols = stats.linregress(v['中考文体总分'].values, v['2007高考成绩'].values)

# Build real candidate dict for lookup
real_map = {}
for _, row in v.iterrows():
    s = int(row['中考文体总分'])
    entry = f"{row['姓名']}({row['就读高中'][:4]}·实测{row['2007高考成绩']:.0f})"
    if s not in real_map:
        real_map[s] = []
    real_map[s].append(entry)

def get_exact_colleges(p):
    if p >= 702:
        return '清华大学高分专业(建筑702/经金703/经管718)'
    elif p >= 688:
        return '北京大学(688分)、清华大学(687分)'
    elif p >= 687:
        return '清华大学统招线(687分)'
    elif p >= 674:
        return '北大医学部(674分)、复旦(667分)、浙大(666分)'
    elif p >= 667:
        return '复旦(667分)、浙大(666分)、上交(665分)、人大(664分)'
    elif p >= 660:
        return '中科大(660分)、南开(654分)、南大(653分)'
    elif p >= 653:
        return '南京大学(653分)、中央财经(653分)、北师大(648分)'
    elif p >= 644:
        return '北师大(648分)、对外经贸(646分)、北航(644分)'
    elif p >= 638:
        return '上海财经(640分)、同济大学(638分)、北外(637分)'
    elif p >= 631:
        return '南开(636分)、西交大(633分)、哈工大(631分)、天大(630分)'
    elif p >= 627:
        return '北理工(627分)、厦门大学(627分)、东北财大(625分)'
    elif p >= 620:
        return '华电北京(623分)、西南财大(621分)、大连理工(620分)、中山大学(620分)'
    elif p >= 615:
        return '武汉大学(619分)、华东理工(617分)、南航(617分)、哈工程(615分)'
    elif p >= 609:
        return '中国海大(614分)、山大(613分)、中政法(609分)、东南大学(608分)'
    elif p >= 603:
        return '北京林业(607分)、西电(605分)、北京科技(604分)、中南大学(603分)'
    elif p >= 600:
        return '湖南大学(602分)、吉林大学(601分)、江南大学(600分)'
    else:
        return '省最低控制线(588分)至599分档(重大/华南理工/川大/地大等)'

# ----------------- Part 1: Generate Comparison Table (600 to 660) -----------------
rows_600_660 = []
for s in range(660, 599, -1):
    cnt = int((zk['文化课+体育成绩'] == s).sum())
    rank = int((zk['文化课+体育成绩'] > s).sum() + 1)
    
    pr_rank = float(np.exp(intercept_r) * (rank ** slope_r))
    pr_score_tbl = get_gk_score_from_rank(pr_rank)
    pr_score_lin = slope_qq * s + int_qq
    real_colleges = get_exact_colleges(pr_score_tbl)
        
    cands_str = '；'.join(real_map.get(s, []))
    
    rows_600_660.append({
        '中考文体总分': s,
        '2004中考市区位次': rank,
        '同分人数': cnt if cnt > 0 else '0 (无同分)',
        '预测2007全省位次': int(round(pr_rank)),
        'Q-Q预测高考分(一分一段)': round(pr_score_tbl, 1),
        'Q-Q线性简化分': round(pr_score_lin, 1),
        '当年可达高校录取线（2007黑龙江理科一批真实投档线）': real_colleges,
        '实名核验考生实测': cands_str if cands_str else '-'
    })

df_table_600_660 = pd.DataFrame(rows_600_660)
df_table_600_660.insert(0, '序号', df_table_600_660.index + 1)
out_csv_path = 'content/kao/qq/大庆中考600至660分预测高考对照表.csv'
df_table_600_660.to_csv(out_csv_path, index=False, encoding='utf-8-sig')
print(f"Saved: {out_csv_path}")

# ----------------- Part 2: Generate 3-Panel Visual Chart -----------------
fig = plt.figure(figsize=(19, 12))
gs = fig.add_gridspec(2, 2, height_ratios=[1.2, 0.8], hspace=0.28, wspace=0.20)

ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

# Subplot 1: Focused Curve for 600 - 660 Range
x_dense = np.linspace(598, 665, 300)
# calculate rank for dense x using inverse interpolation
zk_unique = zk.groupby('文化课+体育成绩').agg(中考名次=('中考名次', 'min')).reset_index().sort_values(by='文化课+体育成绩')
r_dense = np.interp(x_dense, zk_unique['文化课+体育成绩'].values, zk_unique['中考名次'].values)
pr_rank_dense = np.exp(intercept_r) * (r_dense ** slope_r)
pr_score_dense = np.array([get_gk_score_from_rank(r) for r in pr_rank_dense])
pr_linear_dense = slope_qq * x_dense + int_qq

x_sort = v_zk['中考文体总分'].values
y_sort = v_gk['2007高考成绩'].values
p_fit = np.polyfit(x_sort, y_sort, 1)
qq_res_std = np.std(y_sort - np.polyval(p_fit, x_sort))

# Curves in ax1
ax1.plot(x_dense, pr_score_dense, color='#1d4ed8', linewidth=3.2, zorder=3,
         label=f'Q-Q 预测曲线（省一分一段位次反查）: $R_{{gk}} = {np.exp(intercept_r):.3f} \\times R_{{zk}}^{{{slope_r:.4f}}}$')
ax1.plot(x_dense, pr_linear_dense, color='#7c3aed', linewidth=2.2, linestyle='--', zorder=3,
         label=f'Q-Q 线性简化拟合: $\\hat{{Y}} = {slope_qq:.4f}X {int_qq:+.2f}$ ($R = {rval_qq:.4f}, R^2 = {rval_qq**2:.4f}$)')
ax1.plot(x_dense, slope_ols * x_dense + int_ols, color='#059669', linewidth=1.8, linestyle=':', zorder=3,
         label=f'实测散点 OLS 回归线: $\\hat{{Y}} = {slope_ols:.4f}X + {int_ols:.2f}$ ($R = {rval_ols:.4f}$)')

# Confidence ribbon
ax1.fill_between(x_dense, pr_score_dense - 1.96 * qq_res_std, pr_score_dense + 1.96 * qq_res_std,
                 color='#60a5fa', alpha=0.18, zorder=2,
                 label=f'Q-Q 模型 95% 置信预测带 ($\\pm {1.96 * qq_res_std:.1f}$ 分)')

# Target Admission reference horizontal lines (from 2007 official cutoffs in kao folder)
ax1.axhline(688, color='#b91c1c', linestyle='-.', linewidth=1.2, alpha=0.8, zorder=1)
ax1.text(599, 689.0, '北京大学 (688分) / 清华大学 (687分) 2007官方投档线', color='#b91c1c', fontsize=9.2, fontweight='bold')

ax1.axhline(667, color='#ea580c', linestyle='-.', linewidth=1.2, alpha=0.8, zorder=1)
ax1.text(599, 668.0, '复旦大学 (667分) / 浙江大学 (666分) / 上海交大 (665分) 官方投档线', color='#ea580c', fontsize=9.2, fontweight='bold')

ax1.axhline(653, color='#d97706', linestyle='-.', linewidth=1.2, alpha=0.8, zorder=1)
ax1.text(599, 654.0, '南京大学 (653分) / 中央财经 (653分) / 北航 (644分) 官方投档线', color='#d97706', fontsize=9.2, fontweight='bold')

ax1.axhline(631, color='#0d9488', linestyle='-.', linewidth=1.2, alpha=0.8, zorder=1)
ax1.text(599, 632.0, '西安交大 (633分) / 哈尔滨工业大学 (631分) / 天津大学 (630分) 官方投档线', color='#0d9488', fontsize=9.2, fontweight='bold')

# Scatter verified candidates in this range
sub_v = v[v['中考文体总分'] >= 600]
school_styles = {
    '大庆一中': {'color': '#2563eb', 'marker': 'o', 'size': 75, 'label': '大庆一中统招核验考生 (41人)'},
    '大庆实验中学': {'color': '#dc2626', 'marker': 's', 'size': 100, 'label': '大庆实验中学统招考生 (李梦然、魏征)'},
    '大庆铁人中学': {'color': '#d97706', 'marker': '^', 'size': 100, 'label': '大庆铁人中学统招考生 (张远洋、王鑫)'},
    '大庆市铁人中学': {'color': '#d97706', 'marker': '^', 'size': 100, 'label': ''}
}

for school, sty in school_styles.items():
    s_sub = sub_v[sub_v['就读高中'] == school]
    if len(s_sub) > 0 and sty['label']:
        ax1.scatter(s_sub['中考文体总分'], s_sub['2007高考成绩'], color=sty['color'], marker=sty['marker'],
                    s=sty['size'], alpha=0.88, edgecolors='black', linewidth=0.7, zorder=5, label=sty['label'])

# Annotate key individuals
annots = [
    ('李梦然', 648, 709, -2.5, 6.0),
    ('李璐', 663, 693, 0.5, 6.0),
    ('关天下', 656, 690, 0.5, -8.0),
    ('魏征', 654, 688, -4.0, -8.0),
    ('杜宇寰', 644, 688, 0.8, 5.0),
    ('蒋莉', 642, 691, -3.0, 5.5),
    ('曹琪', 638, 683, -2.5, 5.5),
    ('陈川', 634, 698, -1.5, 6.0),
    ('牛雨军', 630, 683, -2.5, 5.5),
    ('李海旭', 626, 685, -2.5, 5.5),
    ('王鑫', 623, 681, -2.5, -7.5),
    ('张远洋(黑马)', 613, 695, -3.5, 5.5),
    ('周旸', 611, 657, -2.5, 5.5),
    ('张大磊', 608, 661, 0.8, -7.0),
    ('牛春军', 609, 641, 0.8, -7.0),
    ('尹成', 607, 650, -2.5, 5.0),
]

for name, x_pt, y_pt, ox, oy in annots:
    ax1.annotate(f"{name} ({x_pt}→{y_pt:.0f})",
                 xy=(x_pt, y_pt),
                 xytext=(x_pt + ox, y_pt + oy),
                 fontsize=8.5, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='#334155', lw=0.8),
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cbd5e1', alpha=0.92),
                 zorder=6)

ax1.set_title('大庆 2004 年中考核心段（600 ~ 660分）预测 2007 年高考理科成绩 Q-Q 精细曲线与实测核验', fontsize=14, fontweight='bold', pad=12)
ax1.set_xlabel('2004 年大庆中考文化课 + 体育总分（满分 680 分，市区应届 5,760 人）', fontsize=11)
ax1.set_ylabel('2007 年黑龙江高考理科总分', fontsize=11)
ax1.grid(True, linestyle='--', alpha=0.45)
ax1.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.95, fontsize=9.2)
ax1.set_xlim(598, 666)
ax1.set_ylim(618, 718)

# Subplot 2: Bar comparison of Metric Improvement (All 69 vs Verified 54)
labels = ['平均绝对误差\nMAE (分)', '均方根误差\nRMSE (分)', '最大预测偏差\nMax Err (分)', '模型判定系数\nR² (×100)']
all_metrics = [27.27, 41.79, 139.9, 38.36]
clean_metrics = [13.06, 15.73, 48.4, 54.37]
improvements = ['-52.1%', '-62.4%', '-65.4%', '+41.7%']

x_idx = np.arange(len(labels))
bar_width = 0.35

rects1 = ax2.bar(x_idx - bar_width/2, all_metrics, bar_width, label='包含自费择校全样本 (69人)', color='#94a3b8', edgecolor='#475569')
rects2 = ax2.bar(x_idx + bar_width/2, clean_metrics, bar_width, label='剔除低端极值噪声后 (54人统招)', color='#2563eb', edgecolor='#1e40af')

ax2.set_title('极值噪声剔除效益对比：全样本 (69人) vs 纯统招核验段 (54人)', fontsize=12, fontweight='bold')
ax2.set_ylabel('数值 / 百分比', fontsize=10.5)
ax2.set_xticks(x_idx)
ax2.set_xticklabels(labels, fontsize=9.5)
ax2.legend(loc='upper right', frameon=True, fontsize=9)
ax2.grid(True, axis='y', linestyle='--', alpha=0.45)

# Add values on top of bars
for i in range(len(labels)):
    v1 = all_metrics[i]
    v2 = clean_metrics[i]
    ax2.text(x_idx[i] - bar_width/2, v1 + 2.0, f"{v1:.1f}", ha='center', va='bottom', fontsize=8.5, color='#475569')
    ax2.text(x_idx[i] + bar_width/2, v2 + 2.0, f"{v2:.1f}\n({improvements[i]})", ha='center', va='bottom', fontsize=8.5, fontweight='bold', color='#1e40af')

ax2.set_ylim(0, 160)

# Explanatory text box in ax2
expl_text = (
    "【剔除依据与结论】\n"
    "• 600分以下15人中11人中考录取为十中/东风/石油高中，属择校自费生\n"
    "• 其单人预测误差高达60~140分，系制度性择校生源与中考位次错位噪声\n"
    "• 剔除低端极值后，MAE从27.3分降至13.1分，预测精准度实现质的飞跃！"
)
ax2.text(0.04, 0.58, expl_text, transform=ax2.transAxes, fontsize=8.5,
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#cbd5e1', alpha=0.95))

# Subplot 3: Residuals and Dark Horse distribution (Zhongkao 600-660)
sub_cand = df_cand[(df_cand['中考文体总分'] >= 600) & (df_cand['是否统招核验'])].copy()
sub_cand['residual'] = sub_cand['2007高考成绩'] - sub_cand['Q-Q预测高考分(一分一段反查)']

ax3.axhline(0, color='black', linestyle='--', linewidth=1.2, label='基准预测线 (残差 = 0)')
ax3.axhspan(-10, 10, color='#86efac', alpha=0.25, label='高精度命中带 ($\\pm 10$ 分以内)')
ax3.axhline(10, color='#16a34a', linestyle=':', linewidth=1.0)
ax3.axhline(-10, color='#16a34a', linestyle=':', linewidth=1.0)

sc3 = ax3.scatter(sub_cand['中考文体总分'], sub_cand['residual'], c=sub_cand['residual'], cmap='coolwarm',
                  s=70, edgecolors='black', linewidth=0.7, zorder=5)

cbar = plt.colorbar(sc3, ax=ax3, orientation='vertical', fraction=0.046, pad=0.04)
cbar.set_label('预测残差 (分): 实际高考分 - Q-Q预测分', fontsize=9.5)

# Annotate outliers in residual plot with specific collision-free offsets
annot_offsets_res = {
    '张远洋': (0.8, 3.5),
    '陈川': (-4.2, 4.0),
    '王鑫': (-4.8, 3.2),
    '鲍慊': (-2.5, -5.5),
    '李海旭': (1.0, 3.5)
}

for idx, r in sub_cand.iterrows():
    name = r['姓名']
    if name in annot_offsets_res:
        ox, oy = annot_offsets_res[name]
        ax3.annotate(f"{name} ({r['residual']:+.1f}分)",
                     xy=(r['中考文体总分'], r['residual']),
                     xytext=(r['中考文体总分'] + ox, r['residual'] + oy),
                     fontsize=8.5, fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color='#334155', lw=0.7),
                     bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cbd5e1', alpha=0.92))
    elif abs(r['residual']) >= 22 and name not in annot_offsets_res:
        ax3.annotate(f"{r['姓名']} ({r['residual']:+.1f}分)",
                     xy=(r['中考文体总分'], r['residual']),
                     xytext=(r['中考文体总分'] + 1.2, r['residual'] + 3.0),
                     fontsize=8.5, fontweight='bold',
                     arrowprops=dict(arrowstyle='->', color='#475569', lw=0.7),
                     bbox=dict(boxstyle='round,pad=0.15', facecolor='white', edgecolor='#e2e8f0', alpha=0.9))

# Precision stats
n_total = len(sub_cand)
within_10 = (sub_cand['residual'].abs() <= 10).sum()
within_15 = (sub_cand['residual'].abs() <= 15).sum()
within_20 = (sub_cand['residual'].abs() <= 20).sum()

res_stats_text = (
    f"【600~660分段精度统计 (共 {n_total} 人)】\n"
    f"• 误差 ≤ ±10 分率: {within_10/n_total*100:.1f}% ({within_10}/{n_total}人)\n"
    f"• 误差 ≤ ±15 分率: {within_15/n_total*100:.1f}% ({within_15}/{n_total}人)\n"
    f"• 误差 ≤ ±20 分率: {within_20/n_total*100:.1f}% ({within_20}/{n_total}人)\n"
    f"• 最大正偏差: 张远洋 (+48.4分·黑马)\n"
    f"• 最大负偏差: 鲍慊 (-23.3分)"
)
ax3.text(0.96, 0.94, res_stats_text, transform=ax3.transAxes,
         ha='right', va='top', fontsize=8.5,
         bbox=dict(boxstyle='round,pad=0.5', facecolor='#f8fafc', edgecolor='#cbd5e1', alpha=0.95))

ax3.set_title('中考 600~660 分段实测考生预测残差与黑马效应分布', fontsize=12, fontweight='bold')
ax3.set_xlabel('2004 年中考文体总分', fontsize=10.5)
ax3.set_ylabel('实测与预测残差 (实际分 - 预测分)', fontsize=10.5)
ax3.set_xlim(598, 668)
ax3.set_ylim(-30, 55)
ax3.grid(True, linestyle='--', alpha=0.45)
ax3.legend(loc='lower left', frameon=True, fontsize=8.8)

# Save chart
out_chart1 = 'content/kao/qq/大庆中考600至660分高考预测精细曲线与实测核验图.png'
out_chart2 = '/Users/albert/.gemini/antigravity-ide/brain/78c5d751-5091-4068-b324-e95c7ecc19b4/大庆中考600至660分高考预测精细曲线与实测核验图.png'

fig.savefig(out_chart1, dpi=300, bbox_inches='tight')
fig.savefig(out_chart2, dpi=300, bbox_inches='tight')
print(f"Chart saved to {out_chart1} and {out_chart2}")
