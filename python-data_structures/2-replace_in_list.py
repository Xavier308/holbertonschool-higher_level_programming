#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specified position if the idx is valid.
    Returns the original list if the index is invalid.
    """
    if 0 <= idx < len(my_list):  # Check if index is within the valid range
        my_list[idx] = element
    return my_list
