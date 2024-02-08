#!/usr/bin/python3
"""scrpt with a function to open a file and print the output"""


def write_file(filename="",text=""):
    """a Fuction to open a file and print out the output"""
    with open(filename,'w',encoding = 'utf-8') as file:
        file.write(text)

    return(len(text))
