#!/usr/bin/python3
str = "Best school"
n = 3
def remove_char_at(str, n):
    copied = str[:]
    get_rid = copied.replace(copied[n], '')
    print(get_rid)


remove_char_at(str,n)
