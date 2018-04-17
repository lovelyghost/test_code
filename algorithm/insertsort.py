# -*- coding: utf-8 -*-
# 插入排序
def insertsort(array):
    
    len_ = len(array)
    for i in range(1,len_):
        print(range(i))
        for j in range(i):
            if array[i] < array[j]:
                print(j)
                array.insert(j,array[i])
                array.pop(i+1)
                break
    return array

print(insertsort([3,5,6,3,4,5,2,5]))