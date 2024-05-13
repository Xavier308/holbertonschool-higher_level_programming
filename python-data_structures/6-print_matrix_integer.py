#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.
    Each row of the matrix is printed on a new line.
    Each integer is printed followed by a space unless it is the
    last integer in the row.
    """
    for row in matrix:
        print(' '.join("{:d}".format(num) for num in row))
