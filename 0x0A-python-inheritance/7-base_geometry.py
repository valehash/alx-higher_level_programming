#!/usr/bin/python3
""" A modulue that builds upon the previous task  """


class BaseGeometry:
    """ A BaseGeometry class."""

    def area(self):
        """ A method that raises an exception. whem the exception is supposed to be raised"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks if the the values passed are valid. or if they are not"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
