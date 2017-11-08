# -*- coding: utf-8 -*-
def binary_search(my_list, item):
    low = 0
    high = len(my_list)-1
    cal_num = 0
    while low <= high:
        cal_num += 1
        mid = (low + high)/2
        guess = my_list[mid]
        if guess == item:
            print cal_num
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = range(128)

print(binary_search(my_list,8))
