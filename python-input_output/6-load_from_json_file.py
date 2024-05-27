#!/usr/bin/python3
"""
This module contains a function that creates an object from a JSON file.
"""

import json


def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the file containing the JSON data.

    Returns:
        object: The Python object created from the JSON data in the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
