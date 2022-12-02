#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied = ''
    value = ''
    if idx < 0 or idx > len(my_list):
        copied = my_list[:]
    else:
        value = my_list[:]
        copied = value
        copied[idx] = element
    return copied
