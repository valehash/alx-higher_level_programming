#!/usr/bin/python3
"""The rectangle class"""
from models.base import Base
class Rectangle(Base):
    """The rectangle class for the aplication"""


    def __init__(self, width, heigth, x=0, y=0, id=None):
        id = super().__init__(id)

        @property
        def get_width(self):
            """returning the value of the width"""
            return self.__width
        
        @width.setter
        def width(self, value):
            """assgining the value of height to self.__width"""
            self.__width = value
        
        @property
        def height(self):
            """returning the value of the height"""
            return self.__height
        @height.setter
        def height(self,value):
            """assgining the value of height to self.__height"""
            self.__height = value
        
        @property
        def y(self):
            """returning the value of y passed by the setter"""
            return self.__y
        @y.setter
        def y(self, value):
            self.__y = value
        
        @property
        def x(self):
            """returning the value of x passed in the getter"""
            return self.__x 
        @x.setter
        def x(self,value):
            self.__x = value
