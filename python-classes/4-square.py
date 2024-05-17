#!/usr/bin/python3
"""
This module defines a class named 'Square' with a private instance
attribute 'size'
that is accessible via a property and can be modified via a setter
with validation.
"""


class Square:
    """
    Defines a square by its 'size', ensuring it's an integer and non-negative,
    with methods to calculate its area and access and modify its size safely.
    """
    def __init__(self, size=0):

        self.__size = size
        """
        Initialize a new Square with size validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
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
