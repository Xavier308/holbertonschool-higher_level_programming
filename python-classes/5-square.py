#!/usr/bin/python3
"""
This module defines a class named 'Square' with a private instance
attribute 'size'
that can be accessed and modified with properties, calculates its area,
and prints
the square using the character '#'.
"""


class Square:
    """
    Defines a square by its 'size', ensuring it's an integer and
    non-negative, with methods to calculate its area, access,
    modify its size, and print itself.
    """
    def __init__(self, size=0):
        """
        Initialize a new Square with size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # Use the setter for initial validation

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
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
