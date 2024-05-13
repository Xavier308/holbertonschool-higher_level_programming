#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Finds and returns the largest integer in the list 'my_list'.
    Returns None if the list is empty.
    """
    if not my_list:
        return None

    # Initialize the maximum value with the first element in the list
    max_value = my_list[0]

    # Iterate through the list
    for number in my_list:
        if number > max_value:
            max_value = number

    return max_value
