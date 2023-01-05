#!/usr/bin/python3
def say_my_name(first_name, last_name=''):
    """Implementing the function.

    Args:
        first_name(str): first parameter
        last_name(str): parameter to be appended to first_name to make full
                        name.
    Raises:
        TypeError: first_name/last_name must be a string

    """
    if not isinstance(first_name, str) and not isinstance(last_name, str):
        raise TypeError('first_name and last_name must be a string')
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
