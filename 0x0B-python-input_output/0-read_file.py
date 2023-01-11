#!/usr/bin/python3

"""reading a file"""


def read_file(filename=''):
    """Implementation
    Args:
        filename(file): file
    Raises:
        Exception
    """
    with open(filename, 'r') as read:
        for line in read.readlines():
            print(line)
