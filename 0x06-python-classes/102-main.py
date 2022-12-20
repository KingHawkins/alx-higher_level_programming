#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if size < 0:
            raise Exception("size must be >= 0")
        elif size >= 0:
            self.size = size
        else:
            raise Exception("size must be integer")


        def size(self):
            return self.size


        def size(self, value):
            if value < 0:
                raise Exception("size must be >= 0")
            elif value >= 0:
                self.size = value
            else:
                raise Exception("size must be an integer")


            def area(self):
                return self.size * self.size
