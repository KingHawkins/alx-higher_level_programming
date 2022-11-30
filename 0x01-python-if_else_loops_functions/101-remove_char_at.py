#!/usr/bin/python3
def remove_char_at(str, n):
    copied = str[:]
    get_rid = ''
    if copied:
        if n < 0 or n > len(copied):
            get_rid = copied[:]
        elif n >= 0:
            get_rid = copied.replace(copied[n], '')
    else:
        get_rid = ''

    return get_rid
