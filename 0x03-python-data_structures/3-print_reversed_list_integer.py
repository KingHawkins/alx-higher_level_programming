#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    value = my_list[::-1]
    for item in range(0, len(my_list), -1):
        print("{:d}".format(my_list[item])
