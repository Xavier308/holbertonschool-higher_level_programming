#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry
(from 7-base_geometry.py), validating width and height as
positive integers.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Instantiates with width and height validated as positive integers.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height, validating them as
        positive integers using the integer_validator from BaseGeometry.

        Args:
            width (int): The width of the rectangle, must be a positive
            integer.
            height (int): The height of the rectangle, must be a positive
            integer.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
