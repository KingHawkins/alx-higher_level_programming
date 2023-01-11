#!/usr/bin/python3

"""Importing json"""
import json

"""Returns dictionary description with simple data str(list, dict\
        string, int, bool) for json serialization of an object
"""


def class_to_json(obj):
    """Implementation of function"""
    return obj.__dict__
