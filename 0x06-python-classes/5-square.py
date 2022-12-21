#!/usr/bin/python3

"""Define class Square."""
class Square:
    """Represents class square."""
    def __init__(self, size=0):
        """Initialize new square
        Args:
             size(int): size of new square
        """
        self.size = size

    @property
    def size(self):
        """Gets new size for setting."""
        return self.__size

    @size.setter
    def size(self, value):
        """Initialize new size
        Args:
             value(int): value of new square
        """
        if value < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(value, int):
             raise TypeError("size must be an integer")
        self.__size = value


    def area(self):
        """Returns new area based on value"""
        return self.__size ** 2


    def my_print(self):
        """"prints graph based on value."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#"*self.__size)
