#!/usr/bin/python3

"""inheriting"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""empty class"""


class Rectangle(BaseGeometry):
    """empty"""
    def __init__(self, width, height):
        """instantiation"""
        self.integer_validator("width", width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
