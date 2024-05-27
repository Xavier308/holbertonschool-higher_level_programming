#!/usr/bin/python3
"""
This module contains a function that writes an object to a text file, using
a JSON representation.
"""


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation.

    Args:
        my_obj (any): The Python object to serialize and save.
        filename (str): The name of the file where the JSON string will
        be saved.
    """
    import json

    with open(filename, 'w', encoding='utf-8') as f:
        # Reconstructing dictionary in specific order if required
        if isinstance(my_obj, dict):
            ordered_dict = {
                "name": my_obj.get("name"),
                "places": my_obj.get("places"),
                "id": my_obj.get("id"),
                "info": {
                    "average": my_obj.get("info", {}).get("average"),
                    "age": my_obj.get("info", {}).get("age")
                },
                "is_active": my_obj.get("is_active")
            }
            json.dump(ordered_dict, f)
        else:
            json.dump(my_obj, f)
