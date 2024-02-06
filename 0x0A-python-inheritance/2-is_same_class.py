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
    if isinstance(obj,a_class):
        return True
    elif not isinstance(obj,a_class):
        return False
