#!/usr/bin/env python3
"""
Defines an abstract class 'Shape' and two subclasses 'Circle' and
'Rectangle'.
Includes a function 'shape_info' that prints area and perimeter of
shapes using duck typing.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract class to represent a geometric shape with methods to calculate
    its area and perimeter.
    """
    @abstractmethod
    def area(self):
        """
        Calculate the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate the perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Represents a circle, implementing the area and perimeter calculations.
    Ensures that the radius provided is non-negative.
    Raises:
        ValueError: If a negative radius is attempted to be set, indicating
        improper use of the class.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Represents a rectangle, implementing the area and perimeter calculations.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Prints the area and perimeter of a shape.
    Relies on duck typing to call the area and perimeter methods of the shape.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
