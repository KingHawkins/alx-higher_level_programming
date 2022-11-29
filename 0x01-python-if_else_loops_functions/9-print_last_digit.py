#!/usr/bin/python3

def print_last_digit(number):
    last_digit = int(str(number)[-1:])
    if number < 0:
        last_digit = -(int(str(number)[-1:]))
    print(last_digit)

print_last_digit(98)
print_last_digit(0)
print_last_digit(-1024)
