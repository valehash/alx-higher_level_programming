#!/usr/bin/python3
"""a function that returns true if the object is a subclass of the class"""


def inherits_from(obj, a_class):
    """
    Parameters:
    -----------
    obj:
        obj is the object that is compared to the class
    a_class:
        a_class is the class comaprsaed against the object
    returns
    --------
    true if the objec is a subclass of the class and false if not
    """
    if type(obj) is not a_class and issubclass(type(obj),a_class):
        return True
    else:
        return False
