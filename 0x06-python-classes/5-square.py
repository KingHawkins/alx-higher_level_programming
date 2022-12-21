#!/usr/bin/python3

"""Define class Square."""
class Square:
    """Represents class square."""
    def __init__(self, size=0):
        """Initialize new square
        Args:
             size(int): size of new square
        """
        if size < 0:
            raise Exception("size must be >= 0")
        elif size >= 0:
            self.size = size
        else:
            raise Exception("size must be integer")

    @property
    def size(self):
        """Gets new size for setting."""
        return self.size

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
        self.size = value


    def area(self):
        """Returns new area based on value"""
        return self.size ** 2


    def my_print(self):
        """"prints graph based on value."""
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#"*self.size)
