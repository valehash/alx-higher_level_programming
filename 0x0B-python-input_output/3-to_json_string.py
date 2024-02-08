#!/usr/bin/python3
"""scrpt with a function to open a file and print the output"""
import json

def to_json_string(my_obj):
    """A Fuction to open a file and print out the output

    Parameters:
    -----------
    my_obj:
        filename holds the name of the file you want to append to
    returns
    --------
        Json string
    -----
    """
    return json.dumps(my_obj)
