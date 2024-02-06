#!/usr/bin/python3
"""a function that returns if the object is from the class"""


def is_same_class(obj, a_class):
    """
    Parameters:
    -----------
    obj:
        obj is the object that is compared to the class
    a_class:
        a_class is the class comaprsaed against the object 
    """
    if type(obj) == a_class and isinstance(obj,a_class):
        return True
    else:
        return False
