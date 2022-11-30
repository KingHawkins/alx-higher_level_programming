#!/usr/bin/python3
def reverse_alt_case():
    res = ''
    for i in range(122, 96, -1):
        if i % 2 != 0:
            res = res + chr(i).upper()
        else:
            res = res + chr(i)
    print("{}".format(res), end='')


reverse_alt_case()
