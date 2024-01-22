#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for k in range(x):
        try:
            print("{}".format(my_list[k]), end = "")
        except IndexError:
            k -= 1
            break
    print()
    return k + 1
