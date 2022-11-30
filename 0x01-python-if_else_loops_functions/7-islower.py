#!/usr/bin/python3
c = 'a'
def islower(c):
    lower_list = [chr(i) for i in range(97, 123)]
    for i in lower_list:
        if c == i:
            value = True
            break
        else:
            value = False

    return value


islower(c)
