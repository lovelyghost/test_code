# -*- coding: utf-8 -*-
#
# def num(n):
#     i = 1
#     while i<=n:
#         yield i**2
#         i+=1
#
# if __name__ == '__main__':
#
#     s = num(4)
#     print(s.next())
#     print(s.next())
#     print(s.close())
#     # print(s.next())

def gen():
    while True:
        a = yield
        print a

b = gen()
b.next() # 直接返回，无输出
b.send(16) # 打印16