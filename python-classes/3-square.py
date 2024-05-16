#!/usr/bin/python3
"""
This module defines a class named 'Square' with a private instance
attribute 'size'
and a public method to calculate the area of the square.
"""


class Square:
    """
    Defines a square by its 'size', ensuring it's an integer and non-negative,
    and allows calculation of its area.
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

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
