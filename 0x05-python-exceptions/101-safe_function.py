#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    fun = ''
    try:
        fun = fct(*args)
        return fun
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
