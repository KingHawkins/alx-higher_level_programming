#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        if mat:
            print(*mat)
        else:
            print("{}".format(''))
