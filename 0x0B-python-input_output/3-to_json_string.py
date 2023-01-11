#!/usr/in/python3

"""Importing json"""
import json

"""json stringifys"""


def to_json_string(my_obj):
    """Implementation
    Args:
        my_obj(object): object
    Raises:
        Exception(FileNotFoundError)
    """
    return json.dumps(my_obj)
