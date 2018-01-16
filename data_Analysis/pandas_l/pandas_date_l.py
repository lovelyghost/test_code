# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import datetime
import calendar


gg = [['2017-12-30', '1', 1111, 1],
 ['2017-12-29', '2', 1185598,1],
  ['2017-12-28', '2', 258568,1],
  ['2017-12-27', '1', 25866,1],
   ['2017-12-26', '2', 258568,1],
  ['2017-12-25', '1', 25766,1]

  ]

dat = pd.DataFrame(gg,columns=['a','b','c','d'])

# def date_deal_start(x):
#   data_split = str(x).split('-')
#   if len(data_split) == 3:
#     _year, _month, _day = data_split
#     start_date = datetime.datetime(int(_year), int(_month), int(_day), 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')
#   else:
#     _year, _month = data_split
#     days = calendar.monthrange(int(_year), int(_month))[1]
#     start_date = datetime.datetime(int(_year), int(_month), 1, 0, 0, 0).strftime('%Y-%m-%d %H:%M:%S')

#   return start_date

# def date_deal_end(x):
#   data_split = str(x).split('-')
#   if len(data_split) == 3:
#     _year, _month, _day = data_split
#     end_date = datetime.datetime(int(_year), int(_month), int(_day), 23, 59, 59).strftime('%Y-%m-%d %H:%M:%S')
#   else:
#     _year, _month = data_split
#     days = calendar.monthrange(int(_year), int(_month))[1]
#     end_date = datetime.datetime(int(_year), int(_month), days, 23, 59, 59).strftime('%Y-%m-%d %H:%M:%S')
#   return end_date

# # 处理时间
# data['e'] = data['a'].map(date_deal_start)
# data['f'] = data['a'].map(date_deal_end)



# data['a'] = pd.to_datetime(data['a'].map(lambda x:x[:10])) + pd.tseries.offsets.DateOffset(days=-1)
# # hh = pd.to_datetime(data['a'])
# print(data['d'][1])
# print(data['a'].max())
# print(data["b"].values)
# print(data)
# def mklbl(prefix,n):
#   return ["%s%s" % (prefix,i)  for i in range(n)]
# miindex = pd.MultiIndex.from_product([mklbl('A',4),
#                                        mklbl('B',2),
#                                        mklbl('C',4),
#                                         mklbl('D',2)])
#
# micolumns = pd.MultiIndex.from_tuples([('a','foo'),('a','bar'),
#                                          ('b','foo'),('b','bah')],
#                                         names=['lvl0', 'lvl1'])
# df = pd.DataFrame(np.arange(len(miindex)*len(micolumns)).reshape((len(miindex),len(micolumns))),
#                      index=miindex,
#                       columns=micolumns).sort_index().sort_index(axis=1)
#
# yy = df["a"][["bar","foo"]]
# print(yy.reset_index())

start = "2017-12-20"
end = "2017-12-30"
date_range_ = pd.date_range(start,end)

date_range_ = pd.DataFrame(date_range_,columns=['a'])
date_range_ = date_range_.astype(str)



data = pd.merge(dat,date_range_,on=['a'],how="outer")
# data = pd.concat([dat,date_range_],ignore_index=True,join_axes=[dat.columns])


print(data)
# print(data)