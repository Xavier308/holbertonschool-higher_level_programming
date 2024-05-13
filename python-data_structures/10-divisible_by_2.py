#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Returns a list of boolean values indicating whether each integer
    in the input list 'my_list' is divisible by 2.
    """
    # Using list comprehension to create a list of True/False values
    return [number % 2 == 0 for number in my_list]
