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
    """
    Defines a square by its 'size' and 'position', ensuring proper validation
    for each and methods to calculate its area and print itself based
    on position.
    """
    def __init__(self, size=0, position=(0, 0)):

        self.size = size
        self.position = position
        """
        Initialize a new Square with size and position validation.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The x and y coordinates of the
            square's position.
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

    @property
    def position(self):
        """
        Retrieve the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the position of the square with validation.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If 'value' is not a tuple of 2 positive integers.
        """
        if not (isinstance(value, tuple) and len(value) == 2 and
                all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Print the square using the character '#' or an empty line if size is 0,
        taking into account its position.
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
