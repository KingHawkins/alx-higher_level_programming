`#!/usr/bin/python3
def fizzbuzz():
    select = ''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end='')
            print(' ', end='')
        elif i % 3 == 0:
            print('Fizz', end='')
            print(' ', end='')
        elif i % 5 == 0:
            if i == 100:
                print('Buzz')
            else:
                print('Buzz', end='')
                print(' ', end='')
        else:
            print(i, end='')
            print(' ', end=''ii


fizzbuzz()
