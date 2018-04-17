# -*- coding: utf-8 -*-

def selectsort(my_list):
    len_ = len(my_list)
    for i in range(len_):
        min_index = i
        # print(min_index)
        for j in range(i+1,len_):
            print(j)
            if my_list[j] < my_list[min_index]:
                min_index = j

        my_list[i],my_list[min_index] = my_list[min_index],my_list[i]
    return my_list
print(selectsort([3,4,2,5,4,7,2]))    