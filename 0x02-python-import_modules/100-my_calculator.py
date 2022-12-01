#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, div, mul
    operator = ['*', '/', '+', '-']
    if len(argv[1:]) < 3 or len(argv[1:]) > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        i = argv[1]
        j = argv[3]
        if argv[2] in operator:
            if argv[2] == '+':
                print("{} + {} = {}".format(i, j, add(int(i), int(j))))
            elif argv[2] == '-':
                print("{} - {} = {}".format(i, j, sub(int(i), int(j))))
            elif argv[2] == '*':
                print("{} * {} = {}".format(i, j, mul(int(i), int(j))))
            else:
                print("{} / {} = {}".format(i, j, div(int(i), int(j))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
