#!usr/bin/python3
def print_reversed_list_integer(my_list=[]):
	count = 0
	lenght = len(my_list)
    if my_list is None:
        return
    else:
	    while(lenght > count):
		    print('{:d}'.format(my_list[lenght - 1]))
		    lenght -= 1

