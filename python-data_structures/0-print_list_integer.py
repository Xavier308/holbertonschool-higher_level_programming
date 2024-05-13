#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """
    Prints all integers in the list `my_list` using str.format().
    Each integer is printed on a new line.
    """
    for number in my_list:
        print("{:d}".format(number))
