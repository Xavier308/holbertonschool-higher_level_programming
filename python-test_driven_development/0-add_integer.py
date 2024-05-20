#!/usr/bin/python3

"""
This module provides the function add_integer, which adds two integers.
The function handles both integers and floats by converting floats to
integers before performing the addition.
"""


def add_integer(a, b=98):
    """
    Add two integers.

    Args:
        a: The first parameter, must be an integer or float.
        b: The second parameter, must be an integer or float. Default is 98.

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast both to integers if they are floats
    a = int(a)
    b = int(b)
    # Return the sum of the two integers
    return a + b
