#!/usr/bin/python3
"""
This module contains a function that writes an object to a text file, using
a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (any): The Python object to serialize and save.
        filename (str): The name of the file where the JSON string will
        be saved.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
