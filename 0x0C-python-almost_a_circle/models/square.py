#!/usr/bin/python3

"""importing rectangle class"""

from .rectangle import Rectangle

"""Inheriting class rectangle"""


class Square(Rectangle):
    """Inheriting"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inheriting"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns string rep of class"""
        return ("[{}] ({}) {}/{} - {}".format(__class__.__name__, self.id,
            self.x, self.y, self.height))

    @property
    def size(self):
        """gets size"""
        return self.width and self.height


    @size.setter
    def size(self, size):
        """sets the width"""
        self.width = size
        self.height = size


    def update(self, *args, **kwargs):
        """overiding update of rectangle class"""
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.height = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[1]
            self.x = args[2]
            self.y = args[3]
        for item in kwargs:
            setattr(self, item, kwargs[item])


    def to_dictionary(self):
        """writes a new dictionary"""
        return{
                "id": self.id,
                "size": self.height,
                "x": self.x,
                "y": self.y
                }
