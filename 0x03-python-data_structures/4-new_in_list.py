#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied = ''
    if idx < 0 or idx >= len(my_list):
        copied = my_list[:]
    else:
        copied = my_list[:]
        copied[idx] = element
    return copied
