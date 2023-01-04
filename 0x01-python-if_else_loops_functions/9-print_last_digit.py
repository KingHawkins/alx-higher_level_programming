#!/usr/bin/python3
def print_last_digit(number):
    last_digit = 0
    if number == 0:
        last_digit = str(0) + str(0)
    elif number > 0:
        last_digit = int(str(number)[-1:] + str(number)[-1:])
    elif number < 0:
        last_digit = int(str(number)[-1:] + str(number)[-1:])
    else:
        last_digit = int(str(number)[-1:])
    print(last_digit)


print_last_digit(98)
