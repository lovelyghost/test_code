# -*- coding: utf-8 -*-


# is and == 的区别
a = "abc"
b = "".join(['a','b','c'])
print("a:",id(a))
print("b:",id(b))
print(a==b)
print(a is b)