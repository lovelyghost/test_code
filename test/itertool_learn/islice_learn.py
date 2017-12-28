# # -*- coding:utf-8 -*-

from itertools import *
import datetime
import time
from collections import defaultdict

# islice
# print 'Stop at 5:'
# for i in islice(count(), 5):
#     print i
#
# print 'Start at 5, Stop at 10:'
# for i in islice(count(), 5, 10):
#     print i
#
# print 'By tens to 100:'
# for i in islice(count(), 0, 100, 10):
#     print i

# groupby
a = ['aa', 'ab', 'abc', 'bcd', 'abcde']
dd = [(10000003L, '\xe6\xb5\x8b\xe8\xaf\x950419', 'saf@10000000830.dt', 1, datetime.datetime(2017, 4, 19, 3, 28, 50, 848439), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'),
 (10013993L, 'fcgxb', 'fgbvcx@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 14, 4, 28, 378077), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'),
  (10013996L, 'hxfgv', 'ghfv@10000000830.dt', 2, datetime.datetime(2017, 12, 25, 16, 0, 32, 987382), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'),
   (10013997L, 'fgxvcgf', 'fxcvdg@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 5, 43, 684407), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'),
    (10013999L, 'gvgfgv', 'zvcfdx@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 14, 9,858956), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'),
    (10013999L, 'gvgfgv', 'zvcfdx@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 14, 9, 858956), None, 'czfd'),
     (10014002L, '123454tgtrdrtvg', 'dszxgfc@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 14, 52, 122183), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'),
      (10014004L, 'rgfdtybvc', 'fcsz@10000000830.dt', 2, datetime.datetime(2017, 12, 25, 16, 15, 10, 139273), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'), 
      (10014005L, 'fesdersf', 'fhyctgh@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 15, 27, 476752), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'),
       (10014007L, 'dxgfvvg', 'fhcbgb@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 15, 43, 942242), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'),
        (10014010L, 'gxcfvyh', 'xgbfycfh@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 16, 2, 89246), None, '\xe4\xb8\x9a\xe5\x8a\xa1\xe5\x91\x98'), 
        (10014010L, 'gxcfvyh', 'xgbfycfh@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 16, 2, 89246), None, 'czfd'),
          (10014000L, 'fdxvgxd', 'fdxv@10000000830.dt', 1, datetime.datetime(2017, 12, 25, 16, 14, 31, 534800), None, None)]


dd = map(list,dd)
ss = time.time()
gg = []
for i,j in groupby(dd,lambda p:p[0]):
    l = list(j)
    if len(l) == 1 and l[0][-1] is None:
        l[0][-1] = "未设置角色"
    if len(l) > 1:
        role = ",".join([e[-1] for e in l])
        l[0].pop()
        l[0].append(role)
    gg.append(l[0])
ee = time.time()
print(ee-ss)


vv = time.time()
sub_range = defaultdict(list)
for i in dd:
    if not sub_range[i[0]]:
        sub_range[i[0]].extend(i)
        if not sub_range[i[0]][6]:
            sub_range[i[0]][6] = "未设置角色"
    else:
        if i[6]:
            role_name = sub_range[i[0]][6]
            sub_range[i[0]][6] = ','.join([role_name, i[6]]) if role_name else i[6]
role_details = sub_range.values()
mm = time.time()
print(mm-vv)




# ff = {str(i):list(j) for i, j in groupby(dd,lambda p:p[0])}
# for i in ff:
#     if 
