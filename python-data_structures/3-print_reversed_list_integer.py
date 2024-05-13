#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers from a list in reverse order, each on a new line.
    """
    for number in reversed(my_list):  # Iterating over the list in reverse
        print("{:d}".format(number))
