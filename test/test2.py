#!/usr/bin/env python
#coding=utf-8
from collections import OrderedDict

#通过某个字段将记录分组

# rows = [
#     {"address":"fuck you ", "date":'12/02/2017'},
#     {"address":"fuck ", "date":'11/02/2017'},
#     {"address":"fuck hha", "date":'14/02/2017'},
#     {"address":"fuck rtha", "date":'16/02/2017'},
#     {"address":"fuck rtha", "date":'12/02/2017'},
#     {"address":"fuck rtha", "date":'14/02/2017'},
# ]
#
# from operator import itemgetter
# from itertools import groupby
# rows.sort(key=itemgetter('date'))
#
# print(rows)
# print("~~~~~~~~~~~~~~")
#
#
# print(groupby(rows,key=itemgetter('date')))
#
# for address, date in groupby(rows,key=itemgetter('date')):
#     print(address)
#     for i in date:
#         print(i)

#过滤序列元素
#
# test_list = [1,2,3,-2,-4,0,'N/A',"-"]
#
# print([n if type(n) == int  else 0 for n in test_list])
#
# def choose(val):
#     try:
#         x=int(val)
#         if x%2==0:
#             return True
#     except ValueError:
#         return False
# print(list(filter(choose,test_list)))
#
# from itertools import compress
# test_list = [1,2,3,-2,-4,0]
# n_test = [n < 0 for n in test_list]
#
# address = ["fuck1","fuck2","fuck3","fuck4","fuck5"]
#
# print(list(compress(address,n_test)))

#从字典中提取子集
# prices = {"s":23,"f":34,"for":45}
# print(prices.items())
# print(prices.keys())
# print(prices.values())
# p1 = {key:what for key, what in prices.items() if what > 30 }
# print(p1)

#映射名称到序列元素



#命名元组序列工厂方法
# from collections import namedtuple
# # Subscriber = namedtuple('subscribe',['add','date'])
# # sub = Subscriber('love never dies','19910208')
# # print(sub)
# # print(sub.add,"|||",sub.date)
# h = ['l' + str(i) for i in range(10) if i in zip([7,8],['mch_id','total_fee'])]
# work = namedtuple('bscribe',['mch_id','total_fee'])
#
# list_t = [(1,1,1,1,1,1,1,1000000111,80,34),(1,1,1,1,1,1,2,1000000123,90,56),(1,1,1,1,1,1,3,1000000143,100,67)]
#
# for index in list_t:
#     n=work(*index)
#     print(tuple(n._replace(total_fee=n.total_fee/100,mch_id=n.mch_id + 3)))


#转换并同时计算数据
# nums = [1,2,3,4,5]
# print(sum(x*x for x in nums))
# print(sum(x*x for x in range(100)))


#合并多个字典和映射
# from collections import ChainMap
# a = {"a":1,"b":2}
# b = {"a":3,"c":4}
# c = ChainMap(a,b)
# print(ChainMap(a,b))
# print(list(ChainMap(a,b)))
# print(len(c))
# print(list(c.keys()))
# print(list(c.values()))
# print(c["b"])
# print(c["a"])
# print(c["c"])
# c=c.parents
# print(c["a"])
import os.path
k = "/Users/lx"
print(os.path.abspath(__file__))
cur_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# dir = os.path.abspath(__file__)
print(cur_dir)
# dir.replace(k,"")
# print(dir.replace(k,""))
# print(cur_dir)
# jj = "wwwwdddd"
# print(jj.replace("ww","e"))

d = {"1":"w","2":"y","3":"u"}
print(",".join(d.values()))
print([d[i] for i in ["1","2"]])