#!/usr/bin/python3
"""
This module adds all arguments to a Python list and then saves them
to a file.
"""

import sys


def save_to_json_file(my_obj, filename):
    """Saves an object to a file using JSON representation."""
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)


def load_from_json_file(filename):
    """Creates an object from a JSON file."""
    import json
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
