#!/usr/bin/python3
"""The python base class"""

class Base:
    """The base class for the aplication"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
