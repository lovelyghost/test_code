# # -*- coding:utf-8 -*-


class demo4:
    def __init__(self, num):
        self.data = num

    def __ror__(self, other):
        return other.data | self.data


s = demo4(3)
f = demo4(9)
h = demo4(4)
print(s | f)
