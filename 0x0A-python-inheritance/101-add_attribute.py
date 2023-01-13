#!/usr/bin/python3

"""adds new attribute to a class"""


def add_attribute(a_class, attr, value):
    """implementing"""
    if (type(a_class)==str or type(a_class)==int or type(a_class)==float
            or type(a_class)==bool or type(a_class)==list
            or type(a_class)==tuple or type(a_class)==dict):
        raise TypeError("can't add new attribute")
    setattr(a_class, attr, value)
