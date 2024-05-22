#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Implements a custom string representation.
    """

    def __init__(self, size):
        """
        Initializes the Square with size, using it for both width and height,
        validated using the integer_validator from Rectangle.

        Args:
            size (int): The size of the square, must be a positive integer.
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size  # Private attribute

    def __str__(self):
        """
        Provides the string representation of the Square.

        Returns:
            str: The string description of the square in the format [Square]
            <width>/<height>.
        """
        return f"[Square] {self.__size}/{self.__size}"

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2


if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
