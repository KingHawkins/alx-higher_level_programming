#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if size < 0:
            raise Exception("size must be >= 0")
        elif position[0] < 0 or position[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        elif size >= 0 or position[0] >= 0 or position[1] >= 0:
            self._size = size
            self._position = (position[0], position[1])
        else:
            raise Exception("size must be integer")


    def size(self):
        return self._size


    def position(self):
        return self._position


    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self._position = (value[0], value[1])


    def size(self, value):
        if value < 0:
           raise Exception("size must be >= 0")
        elif value >= 0:
           self._size = value
        else:
           raise Exception("size must be an integer")


    def area(self):
        return (self._size ** 2)


    def my_print(self):
        if self._size == 0:
           print()
        else:
           for i in range(self._size):
               if self._position[0] >= 0:
                  print(' '*self._position[0] + "#"*self._size)
               else:
                  print("#"*self._size)
