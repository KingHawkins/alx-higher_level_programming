#!/usr/bin/python3

"""inserts a line of text to a file, after each\
        line containing a particular string
"""

def append_after(filename='', search_string='', new_string=''):
    """Implementation"""
    text = ''
    with open(filename, 'r', encoding='utf-8') as out:
        text = out.readlines()
    with open(text, 'a', encoding='utf-8') as inp:
        new = inp.write(
        for item in text:
            if item[len(item)-1] == '\n':
                item[len(item)-1] == '\n' + new_string
                print(''.join(item))
