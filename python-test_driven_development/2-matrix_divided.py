#!/usr/bin/python3
"""
This module contains the function matrix_divided, which divides all elements
of a matrix by a divisor. It checks for matrix uniformity and non-zero divisor,
and returns a new matrix with the results rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor and rounds
    the result to 2 decimal places.

    Args:
        matrix (list of lists of int/float): Matrix to be divided.
        div (int/float): Divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        list: A new matrix with all elements divided by div,
        rounded to 2 decimal places.
    """

    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len({len(row) for row in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
