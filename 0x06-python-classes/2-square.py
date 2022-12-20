#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if int(size) < 0:
            raise Exception("size must be >= 0")
        elif isinstance(size, int) and size >= 0:
            self._size = size
        elif type(size) != int:
            raise Exception("size must be an integer")
