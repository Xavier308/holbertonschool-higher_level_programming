#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specified index.
    If the index is negative or out of range, the list remains unchanged.
    """
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
