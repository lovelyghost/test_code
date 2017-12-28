
import pandas as pd  
import numpy as np
import sys
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


gg = [['100000035155', '1', '112345612345678901111', "3100000035155588433002733375488", '', '1000000351552588434688240128000', 0.01,'\xe9\x80\x80\xe6\xac\xbe\xe6\x88\x90\xe5\x8a\x9f', '\xe6\x94\xaf\xe4\xbb\x98\xe5\xae\x9d', '\xe5\x95\x86\xe6\x88\xb7A', '\xe8\x80\x81\xe7\x8e\x8b123', '\xe5\x95\x86\xe6\x88\xb7A'],
 ['100000035155', '2', '123456123456789011', '3100000035155588379531799826432', '', '1000000351552588381934180241408', 0.01, '\xe9\x80\x80\xe6\xac\xbe\xe6\x88\x90\xe5\x8a\x9f', '\xe6\x94\xaf\xe4\xbb\x98\xe5\xae\x9d', '\xe5\x95\x86\xe6\x88\xb7A', '\xe8\x80\x81\xe7\x8e\x8b123', '\xe5\x95\x86\xe6\x88\xb7A'],
  ['100000035155', '2', 'wx1711101002', '4100000035155588379274940649472', '50000704722017111002297872893', '1000000351552588380406681833472', 0.01, '\xe9\x80\x80\xe6\xac\xbe\xe6\x88\x90\xe5\x8a\x9f', '\xe5\xbe\xae\xe4\xbf\xa1', '\xe5\x95\x86\xe6\x88\xb7A', '\xe8\x80\x81\xe7\x8e\x8b123', '\xe5\x95\x86\xe6\x88\xb7A']]
  
# data = pd.Series(gg) 
# data = np.array(gg) 
# print(data)
save = pd.DataFrame(gg,columns=['商户编号', '创建时间', '商户交易号', '平台交易号', '商户退款单号',
              '平台退款单号', '退款金额', '当前状态', '支付渠道', '商户名称', '所属渠道商', '商户简称'])  

save['创建时间'].replace(to_replace=['1','2'],value=["启用","禁用"],inplace=True)
print(save['创建时间'])
dates = pd.date_range('20130101', periods=6, freq='M')
print(dates)
# save.to_csv('数据分析.csv',index=False,encoding='gb2312',decimal='.')