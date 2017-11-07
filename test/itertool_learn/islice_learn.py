from itertools import *

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
print(groupby(a,len))
for i in groupby(a,len):
    print(i)
for i, k in groupby(a, len):
    type(k)
    print i, list(k)