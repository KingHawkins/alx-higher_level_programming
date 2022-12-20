#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if size < 0:
            raise Exception("size must be >= 0")
        elif position[0] < 0 or position[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        elif size >= 0 or position[0] >= 0 and position[1] >= 0:
            self.size = size
            self.position = (position[0], position[1])
        else:
            raise Exception("size must be integer")


    def size(self):
        return self.size


    def position(self):
        return self.position


    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            raise Exception("position must be a tuple of 2 positive integers")
        else:
            self.position = (value[0], value[1])


    def size(self, value):
            if value < 0:
               raise Exception("size must be >= 0")
            elif value >= 0:
               self.size = value
            else:
                raise Exception("size must be an integer")


    def area(self):
        return self.size * self.size


    def my_print(self):
        if self.size == 0:
           print()
        else:
            for i in range(self.size):
                if self.position[0] > 0:
                    print(' '*self.position[0] + "#"*self.size)
                else:
                    print("#"*self.size)
