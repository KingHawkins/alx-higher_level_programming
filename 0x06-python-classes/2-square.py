#!/usr/bin/python3
"""Define a class Square."""
class Square:
    def __init__(self, size=0):
        """Initialize size
        
        Args:
            size(int): new size
        """
        if int(size) < 0:
            raise Exception("size must be >= 0")
        elif isinstance(size, int) and size >= 0:
            self._size = size
        elif type(size) != int:
            raise Exception("size must be an integer")
