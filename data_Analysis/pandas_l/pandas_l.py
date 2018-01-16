# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

# 声明 series对象
# index 指定标签
s = pd.Series([12,3,4,5,5], index=['a','s','d','g','h'])
print(s)
print(s.values) # 打印值
print(s.index) # 打印标签

# 选择内部元素
print(s[2])
print(s['s'])
print(s[0:3])
print(s[['a','s']])

# 为元素赋值
s[2] = 5
s['s'] = 67
print(s)

# 用 numpy 数组定义series对象
arr = np.array([3,4,5,6,7])
A = pd.Series(arr)
print(A)

# 筛选元素
print(A[A>5])

# series运算函数
print(A/2)
print(np.log(A))

# 获取唯一元素,元素出现次数统计
B = pd.Series([2,3,4,5,6,3,4,5,5])
print(B.unique())
print(B.value_counts())
# isin 判断对象所属关系
print(B.isin([2,3]))

# 判断空值 NAN
C = pd.Series([2,3,4,5,6,3,np.NaN,5,5])
print(C.isnull())
print(C.notnull())
print(C[C.notnull()])

# series用作字典
mydict = {"3":3,"4":5,"6":6}
D = pd.Series(mydict)
myindex = ["3","4","6","j","a"]
E = pd.Series(mydict,index=myindex)
print(E)
print(D)

# series对象之间运算
print(D+E)

# 定义 dataframe
data = {'color':["green","red","purple","yellow","blue"],"num":[1,3,5,7,9],"dont_know":[2,4,6,8,10]}
F = pd.DataFrame(data)
print(F)

# 给 dataframe 指定标签
print(pd.DataFrame(data,index=["a",'b',"c","d","e"]))
print(pd.DataFrame(np.arange(16).reshape((4,4)),index=["a",'b',"c","d"],columns=["green","red","purple","yellow"]))

# 选取 dataframe 元素
print(F.values) # 获取值
print(F.columns) # 获取列标签
print(F.index) # 获取行标签
print(F['num']) # 获取某列的值
print(F.num)
# 获取某行的值
print(F.ix[2])

# 获取多行的值
print(F.ix[[2,3]])
print(F[1:2])

# 获取某个元素
print(F["num"][2])

# 给 dataframe赋值
F["new_c"] = 12 # 赋值单个值
print(F)
F["new_d"] = [7,8,5,3,6] # 赋值列表
print(F)
F["new_e"] = np.array(5) #赋值数组
print(F)
F["new_f"] = pd.Series([9,8,7,6,5]) # 赋值 Series
print(F)

# dataframe 元素所属关系
print(F.isin([1,6]))
print(F[F.isin([1,6])])

# 删除一列
del F["new_f"]
print(F)

# 筛选 dataframe
print(F[F>5])

# 使用潜逃字典生成 dataframe
nestdict = {"red":{2011:1,2013:3},
            "green": {2011: 91, 2012: 7, 2013: 3},
            "re": {2011: 1, 2012: 2, 2013: 7}}
E = pd.DataFrame(nestdict)
print(E)

# dataframe 转置
print(E.T)

# 重建索引 index
H = pd.Series([2,3,4],index=[3,5,7])
print(H)
# H = H.reindex([3,4,6,8]) # reindex方法,将没有的 index 标签去掉,新的标签添加值为 NA
# print(H)
# 重建索引时,新的索引标签填充值有两种方式 method: ffill为复制前索引标签的值, bfill 为复制后面索引值
I = H.reindex([3,4,6,8,9],method="ffill") #
print(I)
