# # -*- coding:utf-8 -*-
# 1 装饰器无参数

class tracer:

    def __init__(self ,func):
        self.calls = 0
        self.func = func

    def __call__(self ,*args):
        self.calls += 1
        print('call %s to %s' %(self.calls, self.func.__name__))
        self.func(*args)


@tracer
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 4)


# 装饰器带参数


class tracer:

    def __init__(self, *args):
        self.calls = 0
        self.args = args

    def __call__(self, func):
        self.func = func
        def realfunc(*args):
            self.calls += 1
            print('call %s to %s' % (self.calls, self.func.__name__))
            self.func(*args)
        return realfunc


@tracer("xxxx")
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 3)
spam(1, 2, 3)

class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):
    print(a + b + c)

spam(1, 2, 3)
spam(1, 2, 3)