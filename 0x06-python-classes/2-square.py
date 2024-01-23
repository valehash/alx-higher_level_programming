#!/usr/bin/python3
"""a class """


class Square:
    """A class with a private instance atribute"""
    pass

    def __init__(self, __size=0):
        """Initializeing with a private instance of size"""
        try:
            __size/1
        except(TypeError):
            print("size must be an integer")
        try:
            __size - 1 > 0
        except (TypeError, ValueError):
            print("size must be >= 0")
    
        self.__size = __size
