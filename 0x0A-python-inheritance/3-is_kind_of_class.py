#!/usr/bin/python3

"""returns true if obj is insubclass of specified class"""


def is_kind_of_class(obj, a_class):
    """Implementing"""
    if isinstance(obj, a_class):
        return True
    return False
