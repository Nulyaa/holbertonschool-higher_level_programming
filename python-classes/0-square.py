#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Squares each element of a matrix (list of lists).

    Args:
        matrix (list): A 2D list (matrix) where each element is a number.

    Returns:
        list: A new matrix (2D list) with each element squared.
    """
    return [[x**2 for x in row] for row in matrix]
