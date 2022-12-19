#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for item in range(x):
            number = number + 1
            print("{:d}".format(my_list[item]), end='')
        print()
        return number
    except IndexError:
        print()
        return number - 1
