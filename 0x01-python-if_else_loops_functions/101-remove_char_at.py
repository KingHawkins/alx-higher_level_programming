#!/usr/bin/python3
def remove_char_at(str, n):
    copied = str[:]
    get_rid = copied.pop(3)
    print(copied)

remove_char_at("Best school", 3)
