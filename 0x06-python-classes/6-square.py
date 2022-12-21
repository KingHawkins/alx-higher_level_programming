#!/usr/bin/python3

"""Define a new class Square."""
class Square:
"""Represents class Square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize new square
        Args:
            size(int): size of new square
            position(int, int): tuple containing the points the square will be plotted
        """
        if size < 0:
            raise Exception("size must be >= 0")
        elif position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        elif not isinstance(size, int):
            raise TypeError("siz must be integer")
        self.size = size
        self.position = (position[0], position[1])

    @property
    def size(self):
        """Gets new size."""
        return self.__size

    @property
    def position(self):
        """Gets position."""
        return self.__position

    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self.__position = (value[0], value[1])

    @size.setter
    def size(self, value):
            if value < 0:
               raise ValueError("size must be >= 0")
            elif isinstance(value, int) and value >= 0:
               self.__size = value
            else:
                raise TypeError("size must be an integer")


    def area(self):
        """Returns new area"""
        return self.__size ** 2


    def my_print(self):
        """Plots the square on a graph."""
        if self.__size == 0:
           print()
        else:
            for i in range(self.__size):
                if self.__position[0] > 0:
                    print(' '*self.__position[0] + "#"*self.__size)
                else:
                    print("#"*self.__size)
