#!/usr/bin/python3
"""
Defines a Rectangle class that inherits from BaseGeometry
(from 7-base_geometry.py).
Includes methods to calculate area and to provide string representation
of the Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.
    Implements area calculation and custom string representation.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height after validating as
        positive integers.

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

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Provides the string representation of the Rectangle.

        Returns:
            str: The string description of the rectangle.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(r.area())
