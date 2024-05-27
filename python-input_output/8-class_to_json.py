#!/usr/bin/python3
"""
This module contains a function that returns the dictionary description with
simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    (list, dictionary, string, integer, and boolean) for JSON
    serialization of an object.

    Args:
        obj: An instance of a Class with potentially serializable attributes.

    Returns:
        A dictionary containing all serializable attributes of obj.
    """
    return obj.__dict__
