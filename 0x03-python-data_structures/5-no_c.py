#!/usr/bin/python3
def no_c(my_string):
    get_rid = ''
    last = ''
    converted = ''
    new = ['c', 'C']
    for i in range(len(my_string)):
        if my_string[i] in new:
            get_rid = list(my_string)
            del get_rid[i]
            continue

    last = ''.join(str(i) for i in get_rid)
    return last
