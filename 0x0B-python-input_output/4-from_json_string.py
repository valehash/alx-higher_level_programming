#!/usr/bin/python3
"""scrpt with a function to open a file and print the output"""
import json

def from_json_string(my_str):
    """A Fuction to open a file and print out the output

    Parameters:
    -----------
    my_str:
        Json string converted to python object
    returns
    --------
        Json string
    -----
    """
    return json.loads(my_str)
