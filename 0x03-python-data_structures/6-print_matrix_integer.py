#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        if mat:
            print("{:d} {:d} {:d} {:d}".format(*mat))
        else:
            print()
