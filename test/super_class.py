# -*- coding:utf-8 -*-
class Root(object):
   def __init__(self):
        print("1")
class B(Root):
   def __init__(self):
        print("2")
        super(B, self).__init__()
        print("3")

class C(Root):
    def __init__(self):
        print("4")
        super(C, self).__init__()
        print("5")

class D(B,C):
    pass
D()