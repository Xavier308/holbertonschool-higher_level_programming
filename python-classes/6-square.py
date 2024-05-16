#!/usr/bin/python3
"""
This module defines a class named 'Square' with a private instance attribute
'size',
a private instance attribute 'position', and includes methods to calculate
its area,
print itself considering its position, and manage these attributes with
properties.
"""


class Square:

    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position

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

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):

        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):

        return self.__size * self.__size

    def my_print(self):

        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
