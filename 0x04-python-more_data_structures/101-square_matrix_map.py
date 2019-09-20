#!/usr/bin/python3
def square_matrix_map(matrix=[]):
        b = map(lambda l: list(map(lambda x: x**2, l)), matrix)
        return list(b)
