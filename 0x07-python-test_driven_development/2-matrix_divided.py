#!/usr/bin/python3
def cumulator(lis, div):
    """Implementation of the function."""
    new = []
    for item in lis:
        new.append(round((item/div), 2))
    return new


def matrix_divided(mat, div):
    """Implementing matrix_divided function.

    Args:
        matrix(list): first parameter
        div(int): divides matrix items

    Raises:
            TypeError: row of matrix must have same size
            ZeroDivisionError: div cannot be zero

    """
    if (not all(isinstance(x, list) for x in mat)
        or not isinstance(mat, list)
        or not all(isinstance(item, list) for item in mat)
        or not all(isinstance(val, (int, float)) for item in mat for val in item)):
            raise TypeError("matrix must be a matrix(list of lists) of integers/floats")
    elif not isinstance(div, (float, int)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif not all(len(mat[0]) == len(item) for item in mat):
        raise TypeError("Each row of matrix must have same size")
    res = []
    for item in mat:
        result = cumulator(item, div)
        res.append(result)
    return res
