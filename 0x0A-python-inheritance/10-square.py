#!/usr/bin/python3

"""Importing rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle

"""Inheriting"""


class Square(Rectangle):
    """Implementating"""
    def __init__(self, size):
        super().__init__(size, size)
        """instantiating
        Args:
            size(int): size of square
        """
        self.integer_validator('size', size)
        self.__size = size


    def area(self):
        """returns area"""
        return self.__size * self.__size
