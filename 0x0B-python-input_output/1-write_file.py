#!/usr/bin/python

"""writes a string to a text file and returns no. of characters written"""

def write_file(filename='', text=''):
    """Implementation
    Args:
        filename(file): name of file to opened
        text(input): text to be written into file
    Raises:
        Exception: if filename does not exist
    """
    number = 0
    with open(filename, 'w', encoding='utf-8') as write_out:
        write_out.write(text)
    with open(filename, 'r', encoding='utf-8') as read_text:
        for character in read_text.read():
            number += 1
    return number
