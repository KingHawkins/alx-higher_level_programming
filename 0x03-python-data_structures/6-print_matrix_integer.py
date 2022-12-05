#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for mat in matrix:
        for item in mat:
            if mat:
               if mat[len(mat) - 1]:
                  print("{:d}".format(item), end='')
            else:
               print("{}".format(''))
