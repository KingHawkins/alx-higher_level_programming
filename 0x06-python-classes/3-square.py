#!/usr/bin/python3

"""Define a class Square."""
class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """Initialize a new square
        Args:
            size(int): new size for square
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(size, int):
            raise TypeError("size must be an integer")
        self._size = size
    
    
    def area(self):
        """Return the area of square"""
        return self._size * self._size
