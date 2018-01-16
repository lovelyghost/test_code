
from pandas import DataFrame,Series
import numpy as np
data = [['pr333','sd23a2','thisisa', '1001', '1005'],
        ['pr33', 'sd23a2', 'sentence', '1001','105'],
        ['pr333', 'sd3a2', 'sentence', '1001', '1005'],
        ['pr333', 'sda2', 'sence', '1001','1005'],
        ['pr333', 'sd23a2', 'sentnce', None, '1005']]

import pandas as pd
# df = pd.read_csv('example.txt',sep=' ',header=None)
df = DataFrame(data,columns=['g','e','r','t','y'])
# df = df[df[4]<>'105']

# print(Series(df[0]).values)
# print(df[0].values)
# print(len(df))
# df = df[df]
df = df.astype(str)
# grouped = df.groupby(['g','e'])

# result = grouped.agg(lambda x:'|'.join(x))

df["t"].replace(to_replace=["None"],value=[np.NaN],inplace=True)
df["r"].replace(to_replace=["sentnce"],value=["zong"],inplace=True)
df["t"].fillna(df["r"],inplace=True)

print(df.to_dict())
# print(result.reset_index())
# print(DataFrame(result))