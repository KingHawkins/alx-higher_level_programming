#!/usr/bin/python3
import json
def from_json_string(my_str):
    """Implementing

    Args:
        my_str(str): string

    Raises:
        Exception

    """
    return json.loads(my_str)
