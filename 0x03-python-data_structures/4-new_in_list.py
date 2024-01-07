#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lenght =  len(my_list)
    if idx < 0 or idx > lenght:
        return my_list
    else:
        copied_list = []
        for i in range(lenght):
            if i == idx:
                copied_list.append(element)
            else:
                copied_list.append(my_list[i])
        
        return copied_list        
