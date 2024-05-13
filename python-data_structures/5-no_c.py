#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all characters 'c' and 'C' from the string 'my_string'.
    Returns the new string without these characters.
    """
    return ''.join(char for char in my_string if char not in ['c', 'C'])
