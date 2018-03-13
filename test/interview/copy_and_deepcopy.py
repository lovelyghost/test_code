# -*- coding: utf-8 -*-

# 对象赋值
ss = [1,2,3,4]
dd = ss
print(u"前",ss,id(ss))
print(u"前",dd,id(dd))
ss.append(5)
print(u"后",ss,id(ss))
print(u"后",dd,id(dd))

# 浅复制
import copy
ss = [1,2,3,[4]]
dd = copy.copy(ss) # 复制了对象,新的引用
print(u"前",ss,id(ss))
print(u"前",dd,id(dd))

ss[3].append(2)
print(u"后",ss,id(ss))
print(u"后",dd,id(dd))

# 深度拷贝

import copy
ss = [1,2,3,[4]]
dd = copy.deepcopy(ss) # 复制了对象,新的引用
print(u"前",ss,id(ss))
print(u"前",dd,id(dd))

ss[3].append(2)
print(u"后",ss,id(ss))
print(u"后",dd,id(dd))

