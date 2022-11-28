#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    a ** b
    a + b
    return 98


dis.dis(magic_calculation)
