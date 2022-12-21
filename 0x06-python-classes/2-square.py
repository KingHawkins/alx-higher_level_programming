#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represent a Square"""
    
    def __init__(self, size=0):
        """Initialize new square
        
        Args:
            size(int): new square
        """
        if size < 0:
            raise ValueError("size must be >= 0")
        elif size >= 0:
            self._size = size
        else:
            raise TypeError("size must be an integer")
