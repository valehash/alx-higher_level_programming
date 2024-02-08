#!/usr/bin/python3
"""scrpt with a function to open a file and print the output"""


def append_write(filename="", text=""):
    """A Fuction to open a file and print out the output

    Parameters:
    -----------
    filename:
        filename holds the name of the file you want to append to
    text:
        the text to be appended to the file
    retruns
    --------
        The lenght if what was appended
    -----
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write("{}".format(text))

    return (len(text))
