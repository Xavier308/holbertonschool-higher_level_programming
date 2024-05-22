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


if __name__ == "__main__":
    r = Rectangle(3, 5)
    print(r)
    print(dir(r))

    try:
        print("Rectangle: {} - {}".format(r.width, r.height))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    try:
        r2 = Rectangle(4, True)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
