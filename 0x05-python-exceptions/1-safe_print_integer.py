#!/usr/bin/python3
def safe_print_integer(value):
    try:
        value/value
        print("{:d}".format(value), end="")
        print()
        return True
    except TypeError:
        return False
