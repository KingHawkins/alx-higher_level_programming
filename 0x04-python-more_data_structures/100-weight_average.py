#!/usr/bin/python3
def converter(a_list):
    res = 0
    accumulator = 0
    for (i, j) in a_list:
        convert = i * j
        res = res + convert
        accumulator = accumulator + j
    final = float(res / accumulator)
    return final


def weight_average(my_list=[]):
    if my_list:
        new = converter(my_list)
        return new
    else:
        return 0
