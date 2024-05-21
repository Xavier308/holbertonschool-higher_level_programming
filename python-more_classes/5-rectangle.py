#!/usr/bin/python3
"""
Defines a Rectangle class with methods for computing area, perimeter,
and handling string representations.
Additionally, it includes a destructor to notify when an
instance is deleted.
"""


class Rectangle:
    """
    A class Rectangle that defines a rectangle by its width and height,
    with additional functionality to detect instance deletion.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the Rectangle instance with optional width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieves the width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the Rectangle
        Throws:
            TypeError: if width is not an integer
            ValueError: if width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieves the height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height of the Rectangle
        Throws:
            TypeError: if height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the Rectangle
        If width or height is 0, the perimeter is 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns the string representation of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        rect_str = []
        for i in range(self.__height):
            rect_str.append("#" * self.__width)
        return "\n".join(rect_str)

    def __repr__(self):
        """
        Returns the official string representation of the Rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Destructor to print a message when a Rectangle instance is deleted
        """
        print("Bye rectangle...")
