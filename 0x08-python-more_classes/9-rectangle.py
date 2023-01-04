#!/usr/bin/python3
"""
Defining class rectangle
"""
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1


    @property
    def width(self):
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
        self.__height = value

    @classmethod
    def square(cls, size=0):
        """makes a square"""
        return cls(size, size)


    def perimeter(self):
        """returns perimeter"""
        return (self.__height + self.__width)*2

    def area(self):
        """returns area"""
        return (self.__height * self.__width)

    def __str__(self):
        for i in range(self.__height):
            print(self.print_symbol*self.__width)
        return ''

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Tests for Equality"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
