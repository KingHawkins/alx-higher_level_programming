#!/usr/bin/python3
def remove_char_at(str, n):
    copied = str[:]
    if n < 0 and copied is True:
        get_rid = copied[:]
    elif n > 0 and copied is True:
        get_rid = copied.replace(copied[n], '')
    else:
        get_rid = ''

    return get_rid
