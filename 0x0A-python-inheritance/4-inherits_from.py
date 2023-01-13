#!/usr/bin/python3

"""returns true if obj is an instance of specified class"""


def inherits_from(obj, a_class):
    """Implementing"""
    if isinstance(obj, a_class):
        return True
    return False
