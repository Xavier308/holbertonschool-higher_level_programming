#!/usr/bin/python3
"""
Determines if an object is exactly an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if the object is exactly an instance of the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj.

    Returns:
        bool: True if obj is exactly an instance of a_class, otherwise False.
    """
    return type(obj) is a_class
