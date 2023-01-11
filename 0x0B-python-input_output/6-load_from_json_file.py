#!/usr/bin/python3

"""importing json"""
import json

"""writes object to a text file"""


def load_from_json_file(filename):
    """Implementing
    Args:
        my_obj(object): object to e parsed to file
        filename(file): file in which obj is written
    """
    with open(filename, 'r', encoding='utf-8') as out:
        return json.load(out)
