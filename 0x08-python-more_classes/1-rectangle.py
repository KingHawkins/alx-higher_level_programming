#!/usr/bin/python3

"""
Defining class rectangle
"""

class Rectangle:
    """Implementing class rectangle"""
    def __init__(self, width=0, height=0):
        """Initialize attributes"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """sets/gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Initializes/sets the width

        Args:
            value(int): value for width

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0

        """
        if not isinstance(value, int):
            raise TypeError("width must be an intager")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value


    @property
    def height(self):
        """Sets/gets height"""
        return self.__height


    @height.setter
    def height(self, value):
        """Initializes the height

        Args:
            value(int): value for the height

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
