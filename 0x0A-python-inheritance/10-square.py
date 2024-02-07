#!/usr/bin/python3
""" A module that builds upon the previous task  """
sq = __import__('9-rectangle').Rectangle


class Square(sq):
    """The rectangle class."""

    def __init__(self, size):
        """The init method for the sqaure class
        Parameters
        -----------
        size:
            The lenght of the square"""

        super().integer_validator("size",size)

    
        self.__size = size
    
    def area(self):
        """The area function that returns the area of the rectangle"""
        area = self.__size ** 2
        return area

    def __str__(self):
        """The str function to displa what the class prints"""

        return "[Rectangle] {}/{}".format(self.__size,self.__size)
