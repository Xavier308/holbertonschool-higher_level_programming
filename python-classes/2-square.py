#!/usr/bin/python3
"""
This module defines a class named 'Square' with a private instance
attribute 'size'.
The class initializes with the 'size' attribute, validating its
type and value.
"""


class Square:

    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
