#!/usr/bin/python3

"""empty class"""


class BaseGeometry:
    """empty"""
    def area(self):
        """Implementation"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """validates an int"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
