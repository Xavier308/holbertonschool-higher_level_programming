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


if __name__ == "__main__":
    a = True
    if inherits_from(a, int):
        print("{} inherited from class {}".format(a, int.__name__))
    if inherits_from(a, bool):
        print("{} inherited from class {}".format(a, bool.__name__))
    if inherits_from(a, object):
        print("{} inherited from class {}".format(a, object.__name__))
