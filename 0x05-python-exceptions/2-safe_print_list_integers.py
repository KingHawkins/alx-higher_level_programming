#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        number = 0
        for item in range(x):
            if isinstance(my_list[item], int):
                print("{:d}".format(my_list[item]), end='')
                number = number + 1
        print()
        return number
    except IndexError:
        print()
        return number
