#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if value:
            print("{:d}".format(value), end='')
        print()
        return True
    except Exception:
        return False
