# # -*- coding:utf-8 -*-
# import cProfile
# import pstats
# def foo():
#     sum=[]
#     for i in range(10000000000000):
#         sum.append(i)
#     print(sum)
#     return sum
# if __name__=="main":
#     cProfile.run("foo()","pro.txt")
#     p = pstats.Stats("pro.txt")
#     p.sort_stats("name").print_stats()
import random
ss = []
for i in range(1000):
    ss.append(random.randint(1, 5))
print(ss)
print(ss.count(1))
print(ss.count(2))