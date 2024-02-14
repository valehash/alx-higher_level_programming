#!/usr/bin/python3
"""The rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The sqaure class for the aplication, which inherits from the rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        


    def __str__(self):
        """function to update the class by changing the return of the function"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,self.y,self.width)

    """def update(self, *args, **kwargs):
        function to update the values passed into the class
        update_list =  ["id", "width", "height", "x", "y"]
        for index in range(len(args)):
            setattr(self, update_list[index], args[index])

        if kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)"""
