#!/usr/bin/python3
"""
This module defines a class named 'Square' with a private instance
attribute 'size'.
The class initializes with the 'size' attribute to define the
dimensions of the square.
"""


class Square:
    """
    Defines a square by its 'size' which is a private instance attribute.
    """
    def __init__(self, size):
        """
        Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
