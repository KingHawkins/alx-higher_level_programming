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
            size(size): size of square
        """
        self.integer_validator('size', size)
        self.__size = size


    def __str__(self):
        """returns str repr of obj"""
        return f'[{__class__.__name__}] {self.__size}/{self.__size}'


    def area(self):
        """returns area"""
        return self.__size * self.__size
