#!/usr/in/python3
import json
def to_json_string(my_obj):
    """Implementation

    Args:
        my_obj(object): object

    Raises:
        Exception(FileNotFoundError)

    """
    return json.dumps(my_obj, indent=None)
