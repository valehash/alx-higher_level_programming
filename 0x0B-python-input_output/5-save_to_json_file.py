#!/usr/bin/python3
"""scrpt with a function to open a file and print the output"""


import json
def save_to_json_file(my_obj, filename):
    """A Fuction to open a file and print out the output

    Parameters:
    -----------
    my_obj:
        The python file being converted to json string
    returns
    --------
        Json string
    -----
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.JSONEncoder().encode(my_obj)
)
