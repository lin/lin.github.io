import pandas as pd
import numpy as np

# Load official 2007 cutoff table
df_cut = pd.read_csv('content/kao/2007年高考黑龙江省本科一批录取分数线及招生人数.csv')
df_cut = df_cut[df_cut['学校名称'] != '省最低控制线（一批）'].copy()

def clean_score(val):
    if pd.isna(val): return None
    val_str = str(val).split('补')[0].split('预')[0].split('蒙')[0].strip()
    try: return float(val_str)
    except: return None

df_cut['score'] = df_cut['理科分数线'].apply(clean_score)
df_cut = df_cut.dropna(subset=['score'])
df_cut['score'] = df_cut['score'].astype(int)

# Create a mapping function for exact reachable colleges
def get_exact_colleges(p):
    if p >= 702:
        return '清华大学热门专业(建筑702/经金703/经管718)'
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
        return '北理工(627分)、厦大(627分)、东财(625分)'
    elif p >= 620:
        return '华电北京(623分)、西财(621分)、大工(620分)、中山(620分)'
    elif p >= 615:
        return '武大(619分)、华东理工(617分)、南航(617分)、哈工程(615分)'
    elif p >= 609:
        return '中国海大(614分)、山大(613分)、中政法(609分)、东南(608分)'
    elif p >= 603:
        return '北林(607分)、西电(605分)、北科大(604分)、中南(603分)'
    elif p >= 600:
        return '湖南大学(602分)、吉林大学(601分)、江南大学(600分)'
    else:
        return '黑龙江省本科一批控制线(588分)以上'

# Test on 600..660
table_df = pd.read_csv('content/kao/qq/大庆中考600至660分预测高考对照表.csv')
table_df['当年可达高校录取线（2007黑龙江理科一批真实投档线）'] = table_df['Q-Q预测高考分(一分一段)'].apply(get_exact_colleges)
if '目标院校参考档次(2007标准)' in table_df.columns:
    table_df = table_df.drop(columns=['目标院校参考档次(2007标准)'])

# Reorder columns
cols = [
    '序号', '中考文体总分', '2004中考市区位次', '同分人数', '预测2007全省位次',
    'Q-Q预测高考分(一分一段)', 'Q-Q线性简化分',
    '当年可达高校录取线（2007黑龙江理科一批真实投档线）',
    '实名核验考生实测'
]
table_df = table_df[cols]
table_df.to_csv('content/kao/qq/大庆中考600至660分预测高考对照表.csv', index=False, encoding='utf-8-sig')
print("Updated content/kao/qq/大庆中考600至660分预测高考对照表.csv successfully")
print(table_df.head(15).to_string())
