import pandas as pd
import numpy as np
from scipy import stats

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
    gk_score = float(r['高考成绩'])
    m = zk[zk['姓名'] == name]
    if len(m) == 0: continue
    
    if len(m) == 1:
        zk_r = m.iloc[0]
    else:
        m_sch = m[m['录取高中'].str.contains(r['高中'][:2], na=False)]
        if len(m_sch) >= 1:
            zk_r = m_sch.iloc[0]
        else:
            m_sc = m[m['文化课+体育成绩'] == r['中考成绩']]
            if len(m_sc) >= 1:
                zk_r = m_sc.iloc[0]
            else:
                zk_r = m.iloc[0]
                
    zk_score = int(zk_r['文化课+体育成绩'])
    zk_rank = int(zk_r['中考名次'])
    gk_rank = score_to_rank_dict.get(int(round(gk_score)), int(round(get_gk_rank_from_score(gk_score))))
    
    candidates.append({
        '姓名': name,
        '就读高中': r['高中'],
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
        '是否统招核验': idx < 55
    })

df_cand = pd.DataFrame(candidates)
print(f'Processed {len(df_cand)} candidates. Verified: {df_cand["是否统招核验"].sum()}')

# Focus on the verified sample for Q-Q model
v = df_cand[df_cand['是否统招核验']].copy()
# Sort for Q-Q
v_zk = v.sort_values(by=['中考文体总分', '2004中考市区名次'], ascending=[False, True]).reset_index(drop=True)
v_gk = v.sort_values(by='2007高考成绩', ascending=False).reset_index(drop=True)

# Power law fit between Zhongkao rank and Gaokao rank
log_r_zk = np.log(v_zk['2004中考市区名次'].values)
log_r_gk = np.log(v_gk['2007高考一分一段名次'].values)
slope_r, intercept_r, rval_r, pval_r, se_r = stats.linregress(log_r_zk, log_r_gk)
print(f'Rank Power-law: ln(R_gk) = {slope_r:.4f} * ln(R_zk) + {intercept_r:.4f}, R={rval_r:.4f}')

# Linear Q-Q fit
slope_qq, int_qq, rval_qq, pval_qq, se_qq = stats.linregress(v_zk['中考文体总分'].values, v_gk['2007高考成绩'].values)
print(f'Linear Q-Q: Y_gk = {slope_qq:.4f} * X_zk + {int_qq:.2f}, R={rval_qq:.4f}')

# Compute predictions for each candidate
pred_ranks = []
pred_scores_table = []
pred_scores_linear = []

for idx, r in df_cand.iterrows():
    # Rank prediction via power-law
    pr_rank = float(np.exp(intercept_r) * (r['2004中考市区名次'] ** slope_r))
    pred_ranks.append(round(pr_rank, 1))
    # Score from 一分一段表
    pr_score_table = get_gk_score_from_rank(pr_rank)
    pred_scores_table.append(round(pr_score_table, 1))
    # Linear score
    pr_score_lin = slope_qq * r['中考文体总分'] + int_qq
    pred_scores_linear.append(round(pr_score_lin, 1))

df_cand['Q-Q预测名次(一分一段位次)'] = pred_ranks
df_cand['Q-Q预测高考分(一分一段反查)'] = pred_scores_table
df_cand['Q-Q线性预测分'] = pred_scores_linear
df_cand['实测与一分一段预测残差'] = np.round(df_cand['2007高考成绩'] - df_cand['Q-Q预测高考分(一分一段反查)'], 1)

print('Sample of updated candidate table:')
print(df_cand[['姓名', '中考文体总分', '2004中考市区名次', '2007高考成绩', '2007高考一分一段名次', 'Q-Q预测名次(一分一段位次)', 'Q-Q预测高考分(一分一段反查)', '实测与一分一段预测残差']].head(15).to_string())
