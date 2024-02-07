#!/usr/bin/python3
""" A module that builds upon the previous task  """
Bg = __import__('7-base_geometry').BaseGeometry


class Rectangle(Bg):
    """The rectangle class."""

    def __init__(self, width, height):
        """The init method for the rectangle class
        Parameters
        -----------
        width:
            The width of the rectangle
        height:
            The height of the rectangle
        """
        
        self.__width = width
        self.__height = height

        super().integer_validator("width", self.__width)
        super().integer_validator("height",self.__height)
        
    
    def area(self):
        """The area function that returns the area of the rectangle"""
        area = self.__width * self.__height
        return area

    def __str__(self):
        """The str function to displa what the class prints"""

        return "[Rectangle]{}/{}".format(self.__width,self.__height)
