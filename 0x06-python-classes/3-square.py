#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if size < 0:
            raise Exception("size must be >= 0")
        elif size >= 0:
            self._size = size
        else:
            raise Exception("size must be an integer")


    def area(self):
        return self._size * self._size
