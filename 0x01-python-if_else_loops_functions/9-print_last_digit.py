#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number > 0:
        last_digit = int(str(number)[-1:])
    if number < 0:
        last_digit = -(int(str(number)[-1:]))
    return last_digit
