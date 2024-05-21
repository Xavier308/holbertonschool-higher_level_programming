#!/usr/bin/python3
"""
This module provides a function called print_square that prints a square of
a given size using the '#' character. It is designed to demonstrate the
handling of basic validation for input types and values
in a straightforward manner.
"""


def print_square(size):
    """
    Prints a square with the character # based on the given size.

    Args:
        size (int): The length of the sides of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.

    Returns:
        None: This function prints directly to standard output.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


# Below lines are just for an example and should not be included in the
# module file if it's used for importing purposes.
# These should be used in a separate test file or main section.
if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
