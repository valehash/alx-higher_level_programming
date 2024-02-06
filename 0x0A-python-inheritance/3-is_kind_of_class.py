#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    if issubclass(obj, a_class):
        return True
    elif not issubclass(obj, a_class):
        return False
