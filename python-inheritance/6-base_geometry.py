#!/usr/bin/python3
"""
Enhances BaseGeometry class with an unimplemented area method.
"""


class BaseGeometry:
    """
    BaseGeometry class with a method area that raises an exception.
    """

    def area(self):
        """
        Raises an Exception with a message indicating that the method is
        not implemented.

        Raises:
            Exception: "area() is not implemented"
        """
        raise Exception("area() is not implemented")
