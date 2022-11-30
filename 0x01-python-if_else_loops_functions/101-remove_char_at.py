#!/usr/bin/python3
def remove_char_at(str, n):
    copied = str[:]
    get_rid = copied.replace(copied[n], '')
    print(get_rid)
