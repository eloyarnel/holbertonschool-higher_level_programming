#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with squared values."""

    return [[x ** 2 for x in row] for row in matrix]
