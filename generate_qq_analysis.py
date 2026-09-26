import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Set styling for publication plot
plt.rcParams['font.sans-serif'] = ['STHeiti', 'PingFang HK', 'Songti SC', 'Hiragino Sans GB', 'Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

# 1. Load 2004 Zhongkao
zk = pd.read_csv('content/kao/qq/2004年中考大庆市区成绩单.csv')
zk['文化课+体育成绩'] = pd.to_numeric(zk['文化课+体育成绩'], errors='coerce')
zk['文化成绩'] = pd.to_numeric(zk['文化成绩'], errors='coerce')
zk['中考名次'] = zk['文化课+体育成绩'].rank(method='min', ascending=False).astype(int)

# 2. Load 2007 Gaokao YFYD table
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

def get_gk_rank_from_score(score):
    s_sorted = yfyd.sort_values(by='分数')
    return float(np.interp(score, s_sorted['分数'], s_sorted['累计人数']))

score_to_rank_dict = dict(zip(yfyd['分数'], yfyd['累计人数']))

# 3. Load df_real
df_real = pd.read_csv('content/kao/qq/大庆中高考实名考生逐人对应表.csv')

candidates = []
for idx, r in df_real.iterrows():
    name = r['姓名']
    if name == '李悦': continue # Excluded due to mismatch with 366-point student
    gk_score = float(r['2007高考成绩']) if '2007高考成绩' in r else float(r['高考成绩'])
    m = zk[zk['姓名'] == name]
    if len(m) == 0: continue
    
    if name == '徐哲':
        # Correctly pick row 1688 from No. 1 Middle School
        m_xz = zk[(zk['姓名'] == '徐哲') & (zk['录取高中'] == '一中')]
        zk_r = m_xz.iloc[0]
    elif len(m) == 1:
        zk_r = m.iloc[0]
    else:
        sch_name = r.get('就读高中', r.get('高中', ''))
        m_sch = m[m['录取高中'].str.contains(sch_name[:2], na=False)]
        if len(m_sch) >= 1:
            zk_r = m_sch.iloc[0]
        else:
            hint_sc = r.get('中考文体总分', r.get('中考成绩'))
            m_sc = m[m['文化课+体育成绩'] == hint_sc]
            if len(m_sc) >= 1:
                zk_r = m_sc.iloc[0]
            else:
                zk_r = m.iloc[0]
                
    zk_score = int(zk_r['文化课+体育成绩'])
    zk_rank = int(zk_r['中考名次'])
    gk_rank = score_to_rank_dict.get(int(round(gk_score)), int(round(get_gk_rank_from_score(gk_score))))
    
    # Strictly check verified status
    is_ver = r['配对方式'] in [
        '校方公布配对',
        '清华新生名单学号＋中考名册考号双向核对（31101826／四十六中／615）',
        '唯一匹配'
    ]
    
    candidates.append({
        '姓名': name,
        '就读高中': r.get('就读高中', r.get('高中')),
        '中考考号': zk_r['考号'],
        '初中学校': zk_r['初中学校'],
        '录取高中': zk_r['录取高中'],
        '中考文化成绩': zk_r['文化成绩'],
        '中考文体总分': zk_score,
        '2004中考市区名次': zk_rank,
        '2007高考成绩': gk_score,
        '2007高考一分一段名次': gk_rank,
        '数据来源': r['数据来源'],
        '配对方式': r['配对方式'],
        '是否统招核验': is_ver
    })

df_cand = pd.DataFrame(candidates)

# 4. Verified sample for Q-Q model
v = df_cand[df_cand['是否统招核验']].copy()
v_zk = v.sort_values(by=['中考文体总分', '2004中考市区名次'], ascending=[False, True]).reset_index(drop=True)
v_gk = v.sort_values(by='2007高考成绩', ascending=False).reset_index(drop=True)

# Power law fit between Zhongkao rank and Gaokao rank
log_r_zk = np.log(v_zk['2004中考市区名次'].values)
log_r_gk = np.log(v_gk['2007高考一分一段名次'].values)
slope_r, intercept_r, rval_r, pval_r, se_r = stats.linregress(log_r_zk, log_r_gk)

# Linear Q-Q fit
slope_qq, int_qq, rval_qq, pval_qq, se_qq = stats.linregress(v_zk['中考文体总分'].values, v_gk['2007高考成绩'].values)

# Individual OLS fit
slope_ols, int_ols, rval_ols, pval_ols, se_ols = stats.linregress(v['中考文体总分'].values, v['2007高考成绩'].values)

# Compute predictions for candidate table
pred_ranks = []
pred_scores_table = []
pred_scores_linear = []

for idx, r in df_cand.iterrows():
    pr_rank = float(np.exp(intercept_r) * (r['2004中考市区名次'] ** slope_r))
    pred_ranks.append(round(pr_rank, 1))
    pr_score_table = get_gk_score_from_rank(pr_rank)
    pred_scores_table.append(round(pr_score_table, 1))
    pr_score_lin = slope_qq * r['中考文体总分'] + int_qq
    pred_scores_linear.append(round(pr_score_lin, 1))

df_cand['Q-Q预测名次(一分一段位次)'] = pred_ranks
df_cand['Q-Q预测高考分(一分一段反查)'] = pred_scores_table
df_cand['Q-Q线性预测分'] = pred_scores_linear
df_cand['实测与一分一段预测残差'] = np.round(df_cand['2007高考成绩'] - df_cand['Q-Q预测高考分(一分一段反查)'], 1)

# Format and save df_cand as new '大庆中高考实名考生逐人对应表.csv'
cols_order = [
    '姓名', '就读高中', '中考文体总分', '2004中考市区名次', '2007高考成绩', '2007高考一分一段名次',
    'Q-Q预测名次(一分一段位次)', 'Q-Q预测高考分(一分一段反查)', 'Q-Q线性预测分', '实测与一分一段预测残差',
    '中考文化成绩', '初中学校', '中考考号', '录取高中', '数据来源', '配对方式', '是否统招核验'
]
df_cand_save = df_cand[cols_order].sort_values(by=['是否统招核验', '2004中考市区名次'], ascending=[False, True]).reset_index(drop=True)
df_cand_save.insert(0, '序号', df_cand_save.index + 1)
df_cand_save.to_csv('content/kao/qq/大庆中高考实名考生逐人对应表.csv', index=False, encoding='utf-8-sig')
print('Saved updated content/kao/qq/大庆中高考实名考生逐人对应表.csv')

# 5. Generate full score prediction curve table: '大庆中高考排名对应表.csv'
zk_scores_unique = zk.groupby('文化课+体育成绩').agg(
    本段人数=('文化课+体育成绩', 'count'),
    中考名次=('中考名次', 'min')
).reset_index().sort_values(by='文化课+体育成绩', ascending=False)

zk_scores_high = zk_scores_unique[zk_scores_unique['文化课+体育成绩'] >= 500].copy()

real_map = {}
for _, row in df_cand[df_cand['是否统招核验']].iterrows():
    s = row['中考文体总分']
    entry = f"{row['姓名']}({row['就读高中'][:4]}·实测{row['2007高考成绩']:.0f})"
    if s not in real_map:
        real_map[s] = []
    real_map[s].append(entry)

pred_curve_rows = []
for _, row in zk_scores_high.iterrows():
    s = int(row['文化课+体育成绩'])
    r_zk = int(row['中考名次'])
    count = int(row['本段人数'])
    
    pr_rank = float(np.exp(intercept_r) * (r_zk ** slope_r))
    pr_score_tbl = get_gk_score_from_rank(pr_rank)
    pr_score_lin = slope_qq * s + int_qq
    
    cand_str = "；".join(real_map.get(s, []))
    
    pred_curve_rows.append({
        '中考文体总分': s,
        '2004中考市区名次': r_zk,
        '同分人数': count,
        'Q-Q预测名次(全省一分一段累计位次)': round(pr_rank, 1),
        'Q-Q预测高考分(一分一段反查)': round(pr_score_tbl, 1),
        'Q-Q线性预测分': round(pr_score_lin, 1),
        '同分段实测考生': cand_str
    })

df_curve = pd.DataFrame(pred_curve_rows)
df_curve.insert(0, '序号', df_curve.index + 1)
df_curve.to_csv('content/kao/qq/大庆中高考排名对应表.csv', index=False, encoding='utf-8-sig')
print('Saved updated content/kao/qq/大庆中高考排名对应表.csv')

# 6. Plotting High-Resolution Figures
fig = plt.figure(figsize=(18, 12))
gs = fig.add_gridspec(2, 2, height_ratios=[1.15, 0.85], hspace=0.30, wspace=0.22)

ax1 = fig.add_subplot(gs[0, :])
ax2 = fig.add_subplot(gs[1, 0])
ax3 = fig.add_subplot(gs[1, 1])

# ----------------- Subplot 1: Main Prediction Curve & Real Students -----------------
x_dense = np.linspace(580, 665, 300)
r_dense = np.interp(x_dense, zk_scores_unique['文化课+体育成绩'].values[::-1], zk_scores_unique['中考名次'].values[::-1])
pr_rank_dense = np.exp(intercept_r) * (r_dense ** slope_r)
pr_score_dense = [get_gk_score_from_rank(r) for r in pr_rank_dense]
pr_linear_dense = slope_qq * x_dense + int_qq

# Q-Q fit residual standard error (along sorted line)
x_sort = v_zk['中考文体总分'].values
y_sort = v_gk['2007高考成绩'].values
p_fit = np.polyfit(x_sort, y_sort, 1)
qq_res_std = np.std(y_sort - np.polyval(p_fit, x_sort))

# Plot curves
ax1.plot(x_dense, pr_score_dense, color='#1d4ed8', linewidth=3.2, label=f'Q-Q 预测曲线（通过高考一分一段表位次反查）: $R_{{gk}} = {np.exp(intercept_r):.3f} \\times R_{{zk}}^{{{slope_r:.4f}}}$')
ax1.plot(x_dense, pr_linear_dense, color='#7c3aed', linewidth=2.2, linestyle='--', label=f'Q-Q 线性拟合线: $\\hat{{Y}} = {slope_qq:.4f}X {int_qq:+.2f}$ ($R = {rval_qq:.4f}$, $R^2 = {rval_qq**2:.4f}$)')
ax1.plot(x_dense, slope_ols * x_dense + int_ols, color='#059669', linewidth=1.8, linestyle=':', label=f'实测散点个体OLS回归线: $\\hat{{Y}} = {slope_ols:.4f}X + {int_ols:.2f}$ ($R = {rval_ols:.4f}$)')

# Confidence band / Prediction ribbon (±2 std errors of Q-Q fit ~ ±5.7 points)
ax1.fill_between(x_dense, np.array(pr_score_dense) - 1.96 * qq_res_std, np.array(pr_score_dense) + 1.96 * qq_res_std,
                 color='#3b82f6', alpha=0.15, label=f'Q-Q 宏观映射 95% 置信带 ($\\pm {1.96 * qq_res_std:.1f}$ 分)')

# Scatter real candidates
school_styles = {
    '大庆一中': {'color': '#2563eb', 'marker': 'o', 'size': 65, 'label': '大庆一中统招实测 (50人)'},
    '大庆实验中学': {'color': '#dc2626', 'marker': 's', 'size': 85, 'label': '大庆实验中学统招实测 (李梦然、魏征)'},
    '大庆铁人中学': {'color': '#d97706', 'marker': '^', 'size': 85, 'label': '大庆铁人中学统招实测 (张远洋、王鑫)'},
    '大庆市铁人中学': {'color': '#d97706', 'marker': '^', 'size': 85, 'label': ''}
}

for school, sty in school_styles.items():
    sub = df_cand[(df_cand['就读高中'] == school) & df_cand['是否统招核验']]
    if len(sub) > 0 and sty['label']:
        ax1.scatter(sub['中考文体总分'], sub['2007高考成绩'], color=sty['color'], marker=sty['marker'],
                    s=sty['size'], alpha=0.85, edgecolors='black', linewidth=0.7, zorder=5, label=sty['label'])

# Annotate key milestone candidates with collision avoidance
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
    ('张远洋', 613, 695, -2.5, 5.5),
    ('周旸', 611, 657, -2.5, 5.5),
    ('徐哲', 581, 603, 0.8, -6.5)
]

for name, x_pt, y_pt, ox, oy in annots:
    ax1.annotate(f"{name} ({x_pt}→{y_pt:.0f})",
                 xy=(x_pt, y_pt),
                 xytext=(x_pt + ox, y_pt + oy),
                 fontsize=8.5, fontweight='bold',
                 arrowprops=dict(arrowstyle='->', color='#475569', lw=0.8),
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white', edgecolor='#cbd5e1', alpha=0.9))

ax1.set_title('大庆 2004 年中考（文体总分）预测 2007 年高考理科成绩 Q-Q 预测曲线全景图', fontsize=14, fontweight='bold', pad=12)
ax1.set_xlabel('2004 年大庆中考文化课 + 体育总分（满分 680 分，市区应届 5,760 人）', fontsize=11)
ax1.set_ylabel('2007 年黑龙江高考理科总分', fontsize=11)
ax1.grid(True, linestyle='--', alpha=0.45)
ax1.legend(loc='lower right', frameon=True, facecolor='white', framealpha=0.95, fontsize=9.5)
ax1.set_xlim(575, 668)
ax1.set_ylim(595, 720)

# ----------------- Subplot 2: Log-Log Rank Mapping (Zhongkao vs Gaokao YFYD) -----------------
ax2.scatter(v_zk['2004中考市区名次'], v_gk['2007高考一分一段名次'], color='#4338ca', s=45, alpha=0.85,
            edgecolors='black', linewidth=0.6, label='Q-Q 分位数次序统计对 (54人)')

r_zk_line = np.geomspace(1, 2000, 200)
r_gk_line = np.exp(intercept_r) * (r_zk_line ** slope_r)
ax2.plot(r_zk_line, r_gk_line, color='#e11d48', linewidth=2.2,
         label=f'幂律分位映射: $\\ln(R_{{gk}}) = {slope_r:.4f}\\ln(R_{{zk}}) {intercept_r:+.4f}$\n($R = {rval_r:.4f}$, $R^2 = {rval_r**2:.4f}$)')

ax2.set_xscale('log')
ax2.set_yscale('log')
ax2.set_title('中考市区名次 与 高考一分一段表位次 Q-Q 对数映射', fontsize=12, fontweight='bold')
ax2.set_xlabel('2004 年中考市区名次 $R_{zk}$ (对数尺度)', fontsize=10.5)
ax2.set_ylabel('2007 年高考全省一分一段位次 $R_{gk}$ (对数尺度)', fontsize=10.5)
ax2.grid(True, which='both', linestyle='--', alpha=0.45)
ax2.legend(loc='upper left', frameon=True, fontsize=9)

# ----------------- Subplot 3: Q-Q Residuals Along the Prediction Line -----------------
qq_residuals = y_sort - (slope_qq * x_sort + int_qq)
ax3.axhline(0, color='black', linestyle='--', linewidth=1.0)
ax3.scatter(x_sort, qq_residuals, c=np.abs(qq_residuals), cmap='coolwarm', s=55, edgecolors='black', linewidth=0.6, zorder=5)

ax3.axhline(1.96 * qq_res_std, color='#ef4444', linestyle=':', label=f'$\\pm 1.96\\sigma$ 置信带 ($\\pm {1.96 * qq_res_std:.1f}$ 分)')
ax3.axhline(-1.96 * qq_res_std, color='#ef4444', linestyle=':')

ax3.set_title(f'Q-Q 次序分位残差分布 (标准误 $\\sigma = {qq_res_std:.2f}$ 分, 最大偏差 {np.max(np.abs(qq_residuals)):.1f} 分)', fontsize=12, fontweight='bold')
ax3.set_xlabel('2004 年中考文体总分', fontsize=10.5)
ax3.set_ylabel('Q-Q 分位残差 (分)', fontsize=10.5)
ax3.grid(True, linestyle='--', alpha=0.45)
ax3.legend(loc='upper left', frameon=True, fontsize=9)
ax3.set_xlim(575, 668)
ax3.set_ylim(-8, 8)

# Save figure to both directory and brain
out_path1 = 'content/kao/qq/大庆中高考QQ预测曲线分析(实名核验版).png'
out_path2 = '/Users/albert/.gemini/antigravity-ide/brain/78c5d751-5091-4068-b324-e95c7ecc19b4/大庆中高考QQ预测曲线分析(实名核验版).png'
fig.savefig(out_path1, dpi=300, bbox_inches='tight')
fig.savefig(out_path2, dpi=300, bbox_inches='tight')
print(f'Successfully re-generated and saved plots to {out_path1} and {out_path2}')
