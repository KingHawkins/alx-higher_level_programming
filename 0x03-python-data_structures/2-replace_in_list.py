#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    value = ''
    if idx < 0 or idx > len(my_list):
        value = my_list
    else:
        value = my_list
        value[idx] = element

    return value
