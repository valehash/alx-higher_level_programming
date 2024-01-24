#!/usr/bin/python3
"""a class """


class Square:
    """A class with a private instance atribute"""
    pass

    def __init__(self, size=0, position=(0, 0)):
        """Initializeing with a private instance of size"""
        self.size = size
        self.position = position

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
    
    
    @property
    def position(self):
        """getter for the position"""
        return self.__position
    
    @position.setter
    def position(self, value):
        """setter for the position"""
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) != int or type(value[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ method to find the area of a square"""
        area =  self.__size ** 2
        return area

    def my_print(self):
        """method to prints  in stdout the square with the character #: and an empty line when size = 0"""
        if self.__size == 0:
            print()

        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
