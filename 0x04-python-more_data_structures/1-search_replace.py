#!/usr/bin/python3
def search_replace(my_list, search, replace):
q    length = len(my_list)
    copied_list = []
    for x in range(length):
        copied_list.append(my_list[x])
        for i, j in enumerate(copied_list):
            if j == search:
                copied_list[i] = replace
    return copied_list
