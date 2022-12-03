#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    value = my_list[::-1]
    for item in value:
        print("{:d}".format(int(item))
