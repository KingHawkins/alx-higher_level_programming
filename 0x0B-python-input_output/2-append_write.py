#!/usr/bin/python3

"""appends a string to end of text file and retruns no. of char added"""

def append_write(filename='', text=''):
    """Implementation.

    Args:
        filename(file): file to be opened
        text(text): text to be written in file

    Raises:
        Exception

    """
    mode = 'a' if filename else 'w'
    with open(filename, mode, encoding='utf-8') as f:
        f.write(text)
        return len(text)
