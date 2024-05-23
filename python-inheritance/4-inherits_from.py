#!/usr/bin/python3
"""
Determines if an object is an instance of a subclass of a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if the object is an instance of a class that inherits from
    the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to check against.

    Returns:
        bool: True if obj is an instance of a subclass of a_class,
        otherwise False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class

