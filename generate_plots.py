import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import os

# Font setup
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'Heiti TC', 'PingFang SC', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['figure.dpi'] = 300

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

# 1. Load data
df_new = pd.read_csv('content/kao/qq/大庆中高考排名对应表.csv')
x_new = df_new['中考成绩'].values
y_new = df_new['高考成绩'].values

# Fit new linear model
res_new = stats.linregress(x_new, y_new)
slope_new, intercept_new, r_new = res_new.slope, res_new.intercept, res_new.rvalue

# Load Daqing No.1 verified
df_yz = pd.read_csv('content/kao/qq/2007年高考大庆一中市区应届中高考成绩.csv')
df_yz = df_yz.dropna(subset=['2004中考成绩', '2007高考总分'])
x_yz = df_yz['2004中考成绩'].values
y_yz = df_yz['2007高考总分'].values

# Suihua verified points
suihua_data = [
    ('陈思 (人大)', 646, 687),
    ('朱天羽 (上交)', 638, 681),
    ('李国一 (哈工大)', 635, 679),
    ('刘滨 (哈工大)', 633, 671),
    ('邢妍 (上交)', 632, 669),
    ('贾洪亮 (北航)', 630, 657),
    ('刘翔 (同济)', 630, 657),
    ('刘欣 (中南财大)', 612, 650)
]

# -------------------- Left Plot: New Macro Q-Q vs Old Distorted Model --------------------
# Plot scatter
ax1.scatter(x_new, y_new, color='#2563eb', alpha=0.6, s=40, edgecolors='none', label='修正后市区应届前239名散点 (N=239)')

# X range for regression
x_range = np.linspace(620, 665, 200)
y_pred_new = slope_new * x_range + intercept_new

# Confidence / prediction interval
y_err = 1.96 * np.std(y_new - (slope_new * x_new + intercept_new))
ax1.fill_between(x_range, y_pred_new - y_err, y_pred_new + y_err, color='#3b82f6', alpha=0.15, label='新模型 95% 置信预测带 (±3.8分)')
ax1.plot(x_range, y_pred_new, color='#1d4ed8', linewidth=2.8, 
         label=f'新宏观预测线: y = {slope_new:.2f}x - {abs(intercept_new):.1f} (R = {r_new:.4f})')

# Old distorted model (two-piece: >=690 and <690)
x_old = np.linspace(628, 665, 200)
y_old = np.where(x_old >= 648, 1.0991 * x_old - 22.60, 2.5637 * x_old - 970.37)
ax1.plot(x_old, y_old, color='#dc2626', linestyle='--', linewidth=2.2, alpha=0.85,
         label='旧宏观模型 (严重高估外县/复读，下段k=2.56骤降至641)')

# Annotate key checkpoints on new line with carefully tuned offsets
pts_cfg = [
    (663, 709, '中考状元李璐\n高考 709分 (全省第3)', (-4.5, -1.0)),
    (643, 680, '680分分水岭 (Rank 31)\n高考 680分 / 中考 643分', (-5.2, 5.0)),
    (637, 668, '中考第93名肖聪\n高考 668分 (旧版仅663)', (1.2, -6.5)),
    (632, 660, '高考660分新切分线 (Rank 168)\n中考 632分 (旧版被推至636)', (-5.5, 4.0)),
    (630, 657, '中考 630分 (Rank 200)\n高考 657分 (旧版跌至644)', (1.0, 3.5)),
    (628, 654, '表底第239名张赢\n高考 654分 (旧版跌至641)', (-2.5, -8.0))
]

for x_pt, y_pt, text, (off_x, off_y) in pts_cfg:
    ax1.plot(x_pt, y_pt, marker='o', markersize=7, color='#d97706', markeredgecolor='black', markeredgewidth=1, zorder=4)
    ax1.annotate(text, (x_pt, y_pt), xytext=(x_pt + off_x, y_pt + off_y),
                 fontsize=8.5, fontweight='bold', color='#1e293b',
                 bbox=dict(boxstyle='round,pad=0.3', fc='#fef3c7', ec='#f59e0b', alpha=0.92),
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.12', color='#b45309', lw=1.2))

ax1.set_title('大庆中高考宏观 Q-Q 预测曲线（生源结构修正前后对比）', fontsize=14, fontweight='bold', pad=14)
ax1.set_xlabel('2004年中考分数（满分680/文化成绩标准）', fontsize=11, labelpad=8)
ax1.set_ylabel('2007年高考理科总分', fontsize=11, labelpad=8)
ax1.set_xlim(624, 666)
ax1.set_ylim(635, 715)
ax1.grid(True, linestyle=':', alpha=0.6)
ax1.legend(loc='upper left', fontsize=9.5, framealpha=0.92)

# -------------------- Right Plot: Real Candidates vs Models --------------------
# Background macro curve
ax2.plot(x_range, y_pred_new, color='#3b82f6', linewidth=2.5, linestyle='-', label=f'修正后宏观基准线 (全市统招期望, k={slope_new:.2f})')

# Daqing No.1 High School linear model (Honors class model: y = 1.1267x - 40.59)
x_yz_range = np.linspace(605, 665, 200)
y_yz_model = 1.1267 * x_yz_range - 40.59
ax2.plot(x_yz_range, y_yz_model, color='#059669', linewidth=2.5, linestyle='-.',
         label='大庆一中尖子班模型: y = 1.13x - 40.6 (加工上限, R=0.988)')

# Scatter Daqing No.1 High real students
ax2.scatter(x_yz, y_yz, color='#10b981', alpha=0.7, s=45, edgecolors='#065f46',
            label='大庆一中实测考生 (N=41，中考公布分与高考实考分)')

# Scatter Suihua verified students
s_names = [s[0] for s in suihua_data]
s_x = [s[1] for s in suihua_data]
s_y = [s[2] for s in suihua_data]
ax2.scatter(s_x, s_y, color='#e11d48', marker='D', s=60, edgecolors='black', linewidth=1.2,
            label='绥化一中重点班实测/高估考生 (陈思646/687, 朱天羽638/681等)')

# Annotate Suihua students
for name, sx, sy in suihua_data:
    offset_y = 4 if sy >= 670 else -11
    offset_x = 0.6
    if sx == 630 and '刘翔' in name: offset_y = -18
    if sx == 612: offset_y = 5; offset_x = -1.2
    ax2.annotate(name, (sx, sy), xytext=(sx + offset_x, sy + offset_y * 0.4),
                 fontsize=8, fontweight='bold', color='#881337',
                 bbox=dict(boxstyle='round,pad=0.25', fc='#ffe4e6', ec='#e11d48', alpha=0.9),
                 arrowprops=dict(arrowstyle='->', color='#be123c', lw=1.0))

# Annotate representative Daqing No.1 students
yz_highlight = [
    ('关天下 (656, 690)', 656, 690, (-3.5, -9)),
    ('曹琪 (638, 683)', 638, 683, (-4.5, 4.5)),
    ('曹明阳 (625, 664)', 625, 664, (-4.5, -9)),
    ('冯聪 (628, 650)', 628, 650, (1.0, -9)),
    ('周旸 (611, 657)', 611, 657, (-4.0, -8))
]
for text, yx, yy, (ox, oy) in yz_highlight:
    ax2.annotate(text, (yx, yy), xytext=(yx + ox, yy + oy),
                 fontsize=7.8, color='#065f46',
                 bbox=dict(boxstyle='square,pad=0.2', fc='#ecfdf5', ec='#10b981', alpha=0.88),
                 arrowprops=dict(arrowstyle='->', color='#059669', lw=0.9))

# Shaded processing advantage zone
ax2.fill_between(x_yz_range, y_yz_model, slope_new * x_yz_range + intercept_new, 
                 where=(y_yz_model >= slope_new * x_yz_range + intercept_new),
                 color='#10b981', alpha=0.08, label='重点名校尖子班超额加工增值区间 (托举增值区)')

ax2.set_title('宏观期望基准 vs 重点班强加工上界（大庆、绥化多源实测对比）', fontsize=14, fontweight='bold', pad=14)
ax2.set_xlabel('2004年中考分数', fontsize=11, labelpad=8)
ax2.set_ylabel('2007年高考理科总分', fontsize=11, labelpad=8)
ax2.set_xlim(605, 666)
ax2.set_ylim(635, 715)
ax2.grid(True, linestyle=':', alpha=0.6)
ax2.legend(loc='lower right', fontsize=9, framealpha=0.92)

plt.tight_layout()

# Save image
out_path_web = 'content/kao/qq/大庆中高考预测曲线分析(修正生源结构).png'
out_path_artifact = '/Users/albert/.gemini/antigravity-ide/brain/04ce830a-5d32-4956-b29f-3478a563cb85/大庆中高考预测曲线分析(修正生源结构).png'

fig.savefig(out_path_web, dpi=300)
fig.savefig(out_path_artifact, dpi=300)
print('Updated plot saved successfully!')
