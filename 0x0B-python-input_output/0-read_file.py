#!/usr/bin/python3

"""reading a file"""

def read_file(filename=''):
    """reading"""
    with open(filename, 'r') as read:
        for line in read.readlines():
            print(line)
