#!/usr/bin/python3

"""Define class square"""
class Square:
    """Represents class square"""
    def __init__(self, size=0):
        """Initialize new square
        Args:
             size(int): size of new square
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize new square
        Args:
             value(int): size of new square
        """
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
            raise TypeError("size must be an integer")
        self.__size = value


    def area(self):
        """Returns area based on size"""
        return self.__size ** 2
