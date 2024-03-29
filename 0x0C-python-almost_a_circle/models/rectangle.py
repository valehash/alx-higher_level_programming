#!/usr/bin/python3
"""The rectangle class"""
from models.base import Base


class Rectangle(Base):
    """The rectangle class for the aplication"""


    def __init__(self, width, height, x=0, y=0, id=None):
        id = super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y


    @property
    def width(self):
        """returning the value of the width"""
        return self.__width
        
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        
    @property
    def height(self):
        """returning the value of the height"""
        return self.__height
        
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
        
    @property
    def y(self):
        """returning the value of y passed by the setter"""
        return self.__y
        
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0") 
        self.__y = value
        
    @property
    def x(self):
        """returning the value of x passed in the getter"""
        return self.__x 
        
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """function that returns the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """function that display a rectangle of width x height with the # symbol"""
        for b in range(self.__y):
            print()
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()
    
    def __str__(self):
        """function to update the class by changing the return of the function"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,self.__y,self.__width,self.__height)

    def update(self, *args, **kwargs):
        """function to update the values passed into the class"""
        update_list =  ["id", "width", "height", "x", "y"]
        for index in range(len(args)):
            setattr(self, update_list[index], args[index])

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """function to display the class attributes as a dictionary""" 
        return {key.lstrip('Rectangle__'): value for key, value in self.__dict__.items()}
