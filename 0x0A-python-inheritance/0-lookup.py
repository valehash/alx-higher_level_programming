#!/usr/bin/python3
"""code to create a function that returns a dictionary of the types the object belongs to"""


def lookup(obj):
    """function that returns the types of an object passed into it as a disctionary."""
    return dir(obj)
