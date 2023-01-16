#!/usr/bin/python3

"""importing base class"""
from .base import Base

"""inheriting base class"""


class Rectangle(Base):
    """Inheriting"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns width"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the new width
        Args:
            width(int, float): new width
        Raises:
            Exception
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """returns height"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the new height
        Args:
            height(int, float): new height
        Raises:
            Exception
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """returns x"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the new value of x
        Args:
            width(int, float): new x
        Raises:
            Exception
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """returns y"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the new value of y
        Args:
            y(int, float): new y
        Raises:
            Exception
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def update(self, *args, **kwargs):
        """updates the rectangle class"""
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id = args[0]
            self.__width = args[1]
        elif len(args) == 3:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
        elif len(args) == 4:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
        elif len(args) >= 5:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        for item in kwargs:
            setattr(self, item, kwargs[item])

    def __str__(self):
        """returns the string rep of object"""
        return ("[{}] ({}) {}/{} - {}/{}".format(__class__.__name__,
                self.id, self.__x, self.__y, self.__width, self.__height))

    def area(self):
        """Returns the area of rectangle"""
        return self.__width * self.__height

    def to_dictionary(self):
        """writes a new dictionary"""
        return {
                "x": self.__x,
                "width": self.__width,
                "id": self.id,
                "height": self.__height,
                "y": self.__y
                }

    def display(self):
        """prints the rectangle"""
        if self.__y > 0:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            print(' '*self.__x + "#"*self.__width)
