#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise type(OSError)
    except BaseException:
        print(message)
