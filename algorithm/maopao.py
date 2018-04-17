# -*- coding: utf-8 -*-



def maopao(my_list):

    list_len = len(my_list)

    for i in range(list_len):
        # print(range(list_len))
        # print(range(0,list_len-i-1))
        for j in range(0,list_len-i-1):
            print(my_list[0:list_len-i-1])
            if my_list[j] > my_list[j+1]:
                my_list[j+1],my_list[j] = my_list[j],my_list[j+1]
                # print(my_list)    
    return my_list
print(maopao([3,2,6,7,1,4,3,6]))
print(range(0))
print(range(0,0))