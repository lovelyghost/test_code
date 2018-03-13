# -*- coding: utf-8 -*-


# 猴子补丁

class myclass:
    def f(self):
        print("fuck")

def monkey_f(self):
    
    print("you")

ff = myclass()
ff.f()
myclass.f = monkey_f
gg = myclass()
gg.f()