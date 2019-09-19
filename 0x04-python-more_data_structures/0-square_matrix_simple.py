#!/usr/in/python3
def square_matrix_simple(matrix=[]):
    if matrix is not None:
        new_matrix = []
        for a in matrix:
            new_matrix.append([])
            for b in a:
                new_matrix[-1].append(b ** 2)
        return new_matrix
