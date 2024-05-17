#!/usr/bin/python3
"""
This module defines a class named 'Square' with a private instance
attribute 'size'.
The class initializes with the 'size' attribute, validating its
type and value.
"""


class Square:
    """
    Defines a square by its 'size', ensuring it's an integer and non-negative.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square with size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If 'size' is not an integer.
            ValueError: If 'size' is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
