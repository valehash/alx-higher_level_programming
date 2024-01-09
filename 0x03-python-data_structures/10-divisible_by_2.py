#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    count = 0
    length = len(my_list)
    new_list = []
    while(count < length):
        if my_list[count] % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
        count +=1
    return new_list
