# # -*- coding:utf-8 -*-
def set_passline(passline):
    def cmp(val):
        if val>= passline:
            print ("pass")
        else:
            print ("failed")
    return cmp
dd = set_passline(90)


def dec(fun):
    def in_dec(*args):
        if len(args)==0:
            return 0
        for i in args:
            if not isinstance(i,int):
                return 0
        return fun(*args)
    return in_dec

# my_sum_= dec(my_sum)
# print(my_sum_(1,2,4,"3"))

@dec
def my_sum(*arg):
    return sum(arg)
print(my_sum(1,2,4,"3"))

