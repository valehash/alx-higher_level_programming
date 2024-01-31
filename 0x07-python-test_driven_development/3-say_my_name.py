#!/usr/bin/python3
"""defines a name printing function"""


def say_my_name(first_name, last_name=""):
    """
    Function to print out the imputed first and last name

    Parameters
    ----------
    first_name
        The first name parameter
    last_name
        The second name parameter

    Returns
    --------
    str
        My name is {first_name} {last_name}
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name ,last_name))
