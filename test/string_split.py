
# -*- coding: utf-8 -*-

for live,_,_,_ in [["生","死","ff","rr"]]:
    print(live)

my_string = '12345678'

answer = [my_string[ll:(ll + 3)] for ll in range(0,len(my_string),3)]
print(answer)

import numpy as np
my_array = [[1,1],[2,2],[3,3]]
arr = np.array(my_array)
print(arr.T)
print(map(list,zip(*my_array)))
print(zip(my_array[0],my_array[1],my_array[2]))

a = [-1,3,2,-5,6]


print(sorted(a,key= lambda x: abs(x),reverse=True))
print(sorted(a,key= lambda x: (-1*x),reverse=True))

print(sorted(a,key= lambda x: x/10 if x > 0 else abs(x)))


def foo(fun):
    def real_fool(*arg,**warg):
        g = fun(*arg,**warg)
        print()
        h = next(g)
        print(h)
        return g
    return real_fool

@foo
def bar():
    for i in range(30):
        yield i


for i in bar():
    print(i)
    # assert isinstance(i, list)