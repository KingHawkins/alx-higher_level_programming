#!/usr/bin/python3
def print_square(size):
    """Implementing.

    Args:
        size(int): length of square

    Raises:
        TypeError: size must be an integer

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise TypeError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#"*size)
