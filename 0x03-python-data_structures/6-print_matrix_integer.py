#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        if len(mat) > 0:
            print("{:d} {:d} {:d}".format(*mat))
        else:
            print('')
