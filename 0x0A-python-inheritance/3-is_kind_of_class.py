#!/usr/bin/python3
"""function that checks if an object is the instance of a class"""
def is_kind_of_class(obj, a_class):
    """
        parameters
        ----------
        obj:
	        The object to be compared against the class
        a_class:
	        The class that is compared to the object
        returns
        -------
	        True if the object is an instance of a class and false where its not
    """
    if isinstance(obj,a_class):
        return True
    elif not isinstance(obj,a_class):
        return False
