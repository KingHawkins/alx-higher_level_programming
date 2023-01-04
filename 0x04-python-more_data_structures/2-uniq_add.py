#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = []
    res = 0
    for item in my_list:
        if item not in new:
            new.append(item)
            res = res + item
    return res
