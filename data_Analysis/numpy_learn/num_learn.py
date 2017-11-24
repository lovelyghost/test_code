# -*- coding:utf-8 -*-


import numpy as np
from numpy import arange
# a = np.array({1, 2, 3})
# print a
#
# dd = np.arange(3)
# print(dd)
# print(range(2))

# def pythonsum(n):
#     a = range(n)
#     b = range(n)
#     c = []
#     for i in range(len(a)):
#         a[i] = i ** 2
#         b[i] = i ** 3
#         c.append(a[i] + b[i])
#     return c
# print(pythonsum(10))

a = arange(24)
print(a)
print(a[3:7])
# 两层楼建筑，每层楼有12个房间，并排列成3行4列
b = a.reshape(2,3,4)
print(b)
# 选定第1层楼、 第1行、第1列的房间
print(b[0,0,0])
# 选取所有楼层的第1行、第1列的房间
# print b[:,0,0]
# 选取第1层楼的所有房间
print(b[0, :, :])
# 用ravel函数完成展平的操作
print(b.ravel())
# flatten就是展平的意思，与ravel函数的功能相同
print(b.flatten())
# 用元组设置维度
g = arange(24)
g.shape = (6,4)
print(g)
# 转置矩阵是很常见的操作
print(g.transpose())


