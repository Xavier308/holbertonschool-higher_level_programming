#!/usr/bin/python3
"""
Checks if an object is an instance of, or inherits from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Determine if an object is an instance of, or is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match against obj.

    Returns:
        bool: True if obj is an instance of a_class or its subclass,
        otherwise False.
    """
    return isinstance(obj, a_class)


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
