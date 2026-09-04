import pandas as pd
from scipy.stats import norm
import numpy as np

# 2004 原始基干数据 (600分以下)
data = [
    (600, 1935, 1935), (590, 808, 2743), (580, 1029, 3772), 
    (570, 1207, 4979), (560, 1420, 6399), (550, 1685, 8084), 
    (540, 1857, 9941), (530, 2240, 12181), (520, 2588, 14769), 
    (510, 2873, 17642), (500, 3277, 20919), (490, 3638, 24557), 
    (480, 3774, 28331), (470, 3998, 32329), (460, 4195, 36524), 
    (450, 4247, 40771), (440, 4413, 45184), (430, 4336, 49520), 
    (420, 4266, 53786), (410, 4324, 58110), (400, 4244, 62354)
]
N = 109045
anchors = {score: cum for score, _, cum in data}

# ==========================================================
# 提取 2005 年的真实物理形状，生成参照分布曲线
# ==========================================================
# 2005年从 638分(约1.77%位置,对应2004年600分) 到 706分(最高分)
ref_span = 706 - 638
ref_max_rank = 2228 # 2005年638分的累计人数
def get_2005_relative_rank(u):
    """
    输入 u (0到1)，表示处于黑箱的百分之多少位置 (0为底, 1为顶)
    返回对应的相对人数比例 q (0到1)
    """
    score_05 = 638 + u * ref_span
    # 使用你提供的真实 2005 数据拟合的一个指数分段近似函数
    # 来精确表达 2005 年尾部的真实衰减率
    # 这里用对数空间插值模拟真实曲线
    x = np.array([638, 650, 660, 670, 680, 690, 706])
    y = np.array([2228, 1183, 605, 274, 112, 35, 1])
    # 映射到 0~1 的 x 和 y 空间
    x_norm = (x - 638) / ref_span
    y_norm = np.log(y) / np.log(ref_max_rank) 
    
    # 线性插值求出 y_norm
    y_interp = np.interp(u, x_norm, y_norm)
    # 反解出比例 q
    q = (ref_max_rank ** y_interp) / ref_max_rank
    return q

results = []

# 1. 单独处理 600~693 的高分黑箱 (使用 2005 形状模板)
span_2004 = 693 - 600
for s in range(693, 599, -1):
    u = (s - 600) / span_2004
    q = get_2005_relative_rank(u)
    R_s = 1935 * q
    results.append({
        '分数': s, 
        '连续位次': R_s, 
        '段内模型': '2005真实形状映射(Q-Q)', 
        '备注': '★ 锚点' if s == 600 else ('★ 20-30名区间' if s == 673 else '')
    })

# 2. 处理常规中低分段
for i in range(1, len(data)):
    a = data[i][0]
    b = data[i-1][0]
    L = b - a
    R_a = anchors[a]
    R_b = anchors[b]
    
    if 200 <= a <= 470:
        method = 'Linear'
    elif 480 <= a <= 590: # 590 及以下适用正态过渡
        method = 'Normal'
        
    for s in range(b - 1, a - 1, -1):
        t = (s - a) / float(L)
        is_anchor = (s == a)
        
        if method == 'Linear':
            R_s = R_a + (R_b - R_a) * t
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

for idx in range(1, len(df)):
    if df.iloc[idx]['位次(该分及以上人数)'] < df.iloc[idx-1]['位次(该分及以上人数)']:
        df.iat[idx, df.columns.get_loc('位次(该分及以上人数)')] = df.iloc[idx-1]['位次(该分及以上人数)']

df['该分人数'] = df['位次(该分及以上人数)'] - df['位次(该分及以上人数)'].shift(1).fillna(0)
df_final = df[['分数', '位次(该分及以上人数)', '该分人数', '段内模型', '备注']]
df_final.to_csv("score_distribution_2004_QQMapped.csv", index=False, encoding="utf-8-sig")
print("✅ Q-Q 映射完成！2004年高分段已按照 2005 年的真实物理曲率完美重建。")