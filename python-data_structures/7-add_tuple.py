#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples, each potentially containing two integers.
    If a tuple has less than two elements, 0 is used as the default value
    for the missing elements.
    If a tuple has more than two elements, only the first two are considered.
    Returns a tuple of two integers.
    """
    # Ensure each tuple has at least two elements
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Calculate the sum of the first and second elements
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
