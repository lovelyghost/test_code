
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


print(sorted(a,key= lambda x: (x<0,abs(x))))



def foo(fun):
    def real_fool(*arg,**warg):
        g = fun(*arg,**warg)

        m_list = [i for i in g]
        final_ = [m_list[ll:(ll + 4)] for ll in range(0,len(m_list),4)]
       
        
        return final_
    return real_fool

@foo
def bar():
    for i in range(30):
        yield i


for i in bar():
    print(i)
    # assert isinstance(i, list)