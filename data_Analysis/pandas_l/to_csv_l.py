# -*- coding: utf-8 -*-

import pandas as pd  
from pandas import DataFrame
import numpy as np
import sys
from numpy import nan as NA
# reload(sys)
# sys.setdefaultencoding('utf8') 
# a = ['one','two','three']  
# b = [1,2,3]  
# english_column = pd.Series(a, name='english')
# print(english_column)  
# number_column = pd.Series(b, name='number')  
# predictions = pd.concat([english_column, number_column], axis=1)  
# #another way to handle  
# save = pd.DataFrame({'english':a,'number':b})  
# print(save)
# save.to_csv('b.csv',index=False,sep=',') 


gg = [['2017-12-29', '1', 1111, 1],
 ['2017-12-29', '2', 1185598,1],
  ['2017-12-28', '2', 258568,1],
  ['2017-12-28', '1', 25866,1],
   ['2017-12-27', '2', 258568,NA],
  ['2017-12-27', '1', 25766,NA],
  ['2017-12-26', '2', 258568,NA],
  ['2017-12-26', '1', 25866,NA],
   ['2017-12-25', '2', 259568,NA],
  ['2017-12-25', '1', 25866,NA],
  ['2017-12-24', '2', 253568,NA],
  ['2017-12-24', '1', 25866,NA],
   ['2017-12-23', '2', 250568,NA],
  ['2017-12-23', '1', 25466,NA],
  ['2017-12-22', '2', 258568,NA],
  ['2017-12-22', '1', 25366,NA],
   ['2017-12-21', '2', 258568,NA],
  ['2017-12-21', '1', 25846,NA],
  ['2017-12-20', '2', 268568,NA],
  ['2017-12-20', '1', 25866,NA]
  ]
  
# data = pd.Series(gg) 
# data = np.array(gg) 
# print(data)
# save = pd.DataFrame(gg,columns=['商户编号', '创建时间', '商户交易号', '平台交易号', '商户退款单号',
#               '平台退款单号', '退款金额', '当前状态', '支付渠道', '商户名称', '所属渠道商', '商户简称'])  

# save['创建时间'].replace(to_replace=['1','2'],value=["启用","禁用"],inplace=True)
# print(save['创建时间'])
# dates = pd.date_range('20130101', periods=6, freq='M')
# print(dates)
# save.to_csv('数据分析.csv',index=False,encoding='gb2312',decimal='.')

data = DataFrame(gg, columns=["pay_time", "balance_type", "profit","dont_know"])
e_p = data[data['balance_type']=="1"][["pay_time","profit","dont_know"]]
p_p = data[data['balance_type']=="2"][["pay_time","profit","dont_know"]]
e_p.rename(columns={'profit':'enterprise_profit'}, inplace = True)
p_p.rename(columns={'profit':'private_profit'}, inplace = True)




# e_p.rename(e_p.pay_time.values)

# e_p.sort_index(axis=1)
# p_p.sort_index(axis=1)

# print(e_p.)
# ep = e_p.reindex(e_p[['pay_time']].values)
# e_p = e_p.set_index(['pay_time']) 重置列
# p_p = p_p.set_index(['pay_time'])
# e_p = e_p.to_dict(orient='records') 转换成字典列表
# p_p = p_p.to_dict(orient='records')


ll = pd.merge(e_p,p_p)
ll.sort_values(by='pay_time')
# print(ll)

# ll = ll.set_index(['pay_time'])
ll[['enterprise_profit', 'private_profit']] = ll[['enterprise_profit', 'private_profit']].applymap(np.round)/100

# ll = ll/100
# ll = ll.round(2)
# ff = 2
# ll = ll.ix[(ff-1)*4:(ff*4-1)]
# ll = np.array(ll).tolist()
# ll = ll.tolist()
# a = list(ll.as_matrix())
enterprise_profit = ll[ll["dont_know"].isnull()]["enterprise_profit"]
ll['dont_know'].fillna(ll['enterprise_profit'],inplace=True)
print(enterprise_profit)
# ll =  pd.merge(ll, enterprise_profit)

print(ll)

# print(ll.to_dict(orient='records'))
# print(e_p)
# print(p_p)
# kk = 
