#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Returns a new list that is a copy of 'my_list' but with the element at
    index 'idx' replaced with 'element'. Does not modify the original list.
    """
    # Create a copy of the list
    list_copy = my_list[:]
    if 0 <= idx < len(list_copy):
        list_copy[idx] = element
    return list_copy
