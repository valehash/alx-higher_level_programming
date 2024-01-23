#!/usr/bin/python3
"""a class """


class Square:
    """A class with a private instance atribute"""
    pass

    def __init__(self, size=0):
        """Initializeing with a private instance of size"""
        self.size = size

    @property
    def size(self):
        """ Getter """
        return self.__size
    @size.setter
    def size(self, value):
        """ Setter """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        """ method to find the area of a square"""
        area =  self.__size ** 2
        return area
