#!/usr/bin/python3
def element_at(my_list, idx):
    value = ''
    if idx < 0 or idx > len(my_list):
        value = None
    else:
        value = my_list[idx]

    return value
