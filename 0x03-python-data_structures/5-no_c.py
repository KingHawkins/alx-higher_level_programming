#!/usr/bin/python3
def no_c(my_string):
    last = ''.join(str(i) for i in my_string if i not in 'Cc')
    return last
