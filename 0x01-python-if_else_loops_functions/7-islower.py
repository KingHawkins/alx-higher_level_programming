#!/usr/bin/python3
def islower(c):
    lower_list = [chr(i) for i in range(97, 123)]
    for i in lower_list:
        if c == '' or isinstance(c, int) is True:
            value = 1
            break
        if c == '"':
            value = 1
        elif c == i:
            value = True
            break
        else:
            value = False

    return value
