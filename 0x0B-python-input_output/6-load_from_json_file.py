#!/usr/bin/python3
"""scrpt with a function to open a file and print the output"""


import json
def load_from_json_file(filename):
    """A Fuction to open a file and print out the output

    Parameters:
    -----------
    filename:
        The file that get's converted to object
    returns
    --------
        Json string
    -----
    """
    with open(filename, 'r', encoding='utf-8') as file:
        to_load = json.load(file)
    return to_load
