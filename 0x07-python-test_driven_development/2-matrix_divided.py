#!/usr/bin/python3
""""Defines matrix_divided.

Args:
    param1(matrix): A list of lists of integers or floats.
    param2(div): a number either integer or float.

Returns:
    The new matrix.

"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix."""
    if matrix is not None:
        new_matrix = []
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = None
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if row_len is None:
            row_len = len(row)
        elif row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if type(col) != int and type(col) != float:
                raise TypeError()
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return list(map(lambda l: list(map(lambda x: round(x / div, 2), l)), matrix))
