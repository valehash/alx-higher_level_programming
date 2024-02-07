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
        width = self.integer_validator("width", width)
        height = self.integer_validator("height",height)
