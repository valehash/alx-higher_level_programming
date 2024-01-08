#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        count = 0
        lenght = len(my_list)
        while(lenght > count):
            print('{:d}'.format(my_list[lenght - 1]))
            lenght -= 1
