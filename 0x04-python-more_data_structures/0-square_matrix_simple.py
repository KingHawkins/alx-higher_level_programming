#!/usr/bin/python3
def square(value):
    new_list = [i ** 2 for i in value]
    return new_list


def square_matrix_simple(matrix=[]):
    new = list(map(square, matrix))
    return new
