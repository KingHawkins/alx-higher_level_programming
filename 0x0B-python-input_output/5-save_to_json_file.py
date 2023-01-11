#!/usr/bin/python3
import json

"""writes object to a text file"""

def save_to_json_file(my_obj, filename):
    """Implementing

    Args:
        my_obj(object): object to e parsed to file
        filename(file): file in which obj is written

    """
    with open(filename, 'w', encoding='utf-8') as out:
        json.dump(my_obj, out)
