#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    num = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end = "")
            num = num + 1
        except (ValueError, TypeError):
            continue
    print()
    return num
