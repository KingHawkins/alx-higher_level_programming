#!/usr/bin/python3
def remove_char_at(str, n):
    copied = str[:]
    if n < 0:
        get_rid = copied.replace(copied[:-n], '')
    else:
        get_rid = copied.replace(copied[n], '')

    return get_rid
