import pandas as pd
import numpy as np

df5 = pd.read_csv('stay_time2.csv')

df5_s = df5.drop(['stay_id'], axis = 1)#열 삭제

df5_s.drop(df5_s.index[148:757], inplace=True)# 여백행 삭제

# df5_s = df5_s.sort_values(by=["stay_time"], ascending=[False])#내림차순

## 데이터 리스트 이름 = data_list 로 사용
data_list = df5_s['stay_time'].values.tolist()

