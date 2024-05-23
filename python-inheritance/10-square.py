#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    Instantiates with size validated as a positive integer.
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

    def __str__(self):
        """
        Provides the string representation of the Square.

        Returns:
            str: The string description of the square.
        """
        width = self._Rectangle__width
        height = self._Rectangle__height
        description = f"[Rectangle] {width}/{height}"
        return description

