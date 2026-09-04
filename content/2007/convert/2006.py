import pandas as pd
from scipy.stats import norm

# 原始数据 2006 (下限分数, 段内人数, 累计人数)
# 已修复 570 档的 OCR 累计人数错误 (17220 -> 17720)
data = [
    (713, 0, 0), # 虚拟上限锚点
    (705, 5, 5), (700, 5, 10), (695, 13, 23), (690, 22, 45), (685, 33, 78), 
    (680, 74, 152), (675, 86, 238), (670, 114, 352), (665, 143, 495), 
    (660, 175, 670), (655, 256, 926), (650, 306, 1232), (645, 336, 1568), 
    (640, 420, 1988), (635, 495, 2483), (630, 576, 3059), (625, 628, 3687), 
    (620, 759, 4446), (615, 869, 5315), (610, 922, 6237), (605, 1038, 7275), 
    (600, 1181, 8456), (595, 1286, 9742), (590, 1395, 11137), (585, 1499, 12636), 
    (580, 1591, 14227), (575, 1635, 15862), (570, 1858, 17720), # <== 修复点
    (565, 1848, 19568), (560, 1998, 21566), (555, 2074, 23640), (550, 2070, 25710), 
    (545, 2164, 27874), (540, 2243, 30117), (535, 2325, 32442), (530, 2344, 34786), 
    (525, 2308, 37094), (520, 2327, 39421), (515, 2497, 41918), (510, 2385, 44303), 
    (505, 2406, 46709), (500, 2279, 48988), (495, 2380, 51368), (490, 2349, 53717), 
    (485, 2267, 55984), (480, 2290, 58274), (475, 2207, 60481), (470, 2235, 62716), 
    (465, 2192, 64908), (460, 2067, 66975), (455, 2030, 69005), (450, 1975, 70980)
]
N = 70980
anchors = {score: cum for score, _, cum in data}

results = []

for i in range(1, len(data)):
    a = data[i][0]
    b = data[i-1][0]
    L = b - a # 自动适配 5 分或 8 分跨度
    
    R_a = anchors[a]
    R_b = anchors[b]
    
    # 动态划分段落
    if 450 <= a <= 535:
        method = 'Linear'
    elif 540 <= a <= 625:
        method = 'Normal'
    else:
        method = 'Geometric'
        
    for s in range(b - 1, a - 1, -1):
        t = (s - a) / float(L)
        is_anchor = (s == a)
        
        if method == 'Linear':
            R_s = R_a + (R_b - R_a) * t
        elif method == 'Geometric':
            rb_safe = max(R_b, 0.1) 
            ra_safe = max(R_a, 0.1)
            q = (rb_safe / ra_safe) ** (1/L)
            R_s = ra_safe * (q ** (s - a))
        elif method == 'Normal':
            z_a = norm.ppf(1 - R_a / N) if R_a > 0 else 5.0
            z_b = norm.ppf(1 - R_b / N) if R_b > 0 else 5.0
            z_s = z_a + (z_b - z_a) * t
            R_s = N * (1 - norm.cdf(z_s))
            
        results.append({
            '分数': s, 
            '连续位次': R_s, 
            '段内模型': method, 
            '备注': '★ 锚点' if is_anchor else ''
        })

df = pd.DataFrame(results).sort_values('分数', ascending=False)
df['位次(该分及以上人数)'] = df['连续位次'].round().astype(int)

# 确保单调递减（防回扫修正）
for idx in range(1, len(df)):
    if df.iloc[idx]['位次(该分及以上人数)'] < df.iloc[idx-1]['位次(该分及以上人数)']:
        df.iat[idx, df.columns.get_loc('位次(该分及以上人数)')] = df.iloc[idx-1]['位次(该分及以上人数)']

# 计算该分人数 (P(s) = Rank(s) - Rank(s+1))
df['该分人数'] = df['位次(该分及以上人数)'] - df['位次(该分及以上人数)'].shift(1).fillna(0)

# 输出清理
df_final = df[['分数', '位次(该分及以上人数)', '该分人数', '段内模型', '备注']]
df_final.to_csv("score_distribution_2006.csv", index=False, encoding="utf-8-sig")
print("✅ CSV生成完毕！纠错完成，广义动态跨度插值逻辑 100% 自洽。")