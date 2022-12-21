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
        elif not isinstance(value, int) or not isinstance(value, float):
            raise TypeError("size must be a number")
        self.__size = value


    def area(self):
        """Returns area based on size"""
        return self.__size ** 2

 
    def __eq__(self, other):
        """Define the == comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the != comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the < comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the <= comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the > comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the >= compmarison to a Square."""
        return self.area() >= other.area()
