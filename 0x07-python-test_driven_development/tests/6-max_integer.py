#!/usr/bin/python3
def max_integer(lis=[]):
    """Implementing

    Args:
        list(list): parameter

    Raises:
        TypeError: must be a list

    """
    if not isinstance(lis, list):
        raise TypeError("must be a list item")
    if len(lis) == 0:
        return None
    elif len(lis) == 1:
        return lis[0]
    max_integer = lis[0]
    for item in lis:
        if item > max_integer:
            max_integer = item
    return max_integer
