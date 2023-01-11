#!/usr/bin/python3

"""Imprting json"""
import json

"""reads json string"""


def from_json_string(my_str):
    """Implementing
    Args:
        my_str(str): string
    Raises:
        Exception
    """
    return json.loads(my_str)
