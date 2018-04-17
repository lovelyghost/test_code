# -*- coding: utf-8 -*-

def quicksorted(array):
    
    if len(array) < 2:
        return array
    first_num = array[0]
    left_ = [i for i in array[1:] if i < first_num]
    right_ = [i for i in array[1:] if i >= first_num]

    return quicksorted(left_) + [first_num] + quicksorted(right_)

print(quicksorted([5,6,3,7,8,4,2,6,8]))
