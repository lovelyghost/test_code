# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-

# class YH(object):
#     def __init__(self,ff):
#         self.ff =ff
#
# if __name__ == '__main__':
#     dd = YH(3)
#     print(dd.ff)
#
#


class Student(object):

    def __init__(self,name,gender):
        self._name = name
        self._gender = gender

    def get_name(self):
        return self._name

    def get_gender(self):
        return self._gender

    def set_name(self,name):
        self._name = name

    def set_gender(self,gender):
        self._gender = gender


#测试
bart = Student("ee", 56)

print('bart.get_name() =',bart.get_name())