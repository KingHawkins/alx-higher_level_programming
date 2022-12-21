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
        self.size = size
        self.position = position

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
        if value[0] < 0 or value[1] < 0  or
            not isinstance(value, tuple) or
            len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
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
