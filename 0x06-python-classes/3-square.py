#!/usr/bin/python3
"""a class """


class Square:
    """A class with a private instance atribute"""
    pass

    def __init__(self, size=0):
        """Initializeing with a private instance of size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Method to get th area of a class"""
        area = self.__size**2
        return area
