#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    value = my_list[::-1]
    for int(item) in value:
        print("{:d}".format(item))
