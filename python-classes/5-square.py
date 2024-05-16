#!/usr/bin/python3
"""
This module defines a class named 'Square' with a private instance
attribute 'size'
that can be accessed and modified with properties, calculates its area,
and prints
the square using the character '#'.
"""


class Square:

    def __init__(self, size=0):

        self.size = size  # Use the setter for initial validation

    @property
    def size(self):

        return self.__size

    @size.setter
    def size(self, value):

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):

        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character '#' or an empty line if size is 0.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
