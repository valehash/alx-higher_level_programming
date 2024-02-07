#!/usr/bin/python3
"""scrpt with a function to open a file and print the output"""


def read_file(filename=""):
    """a Fuction to open a file and print out the output"""
    with open(filename,'r',encoding = 'utf-8') as file:
        for line in file:
            print(line, end='')
