#!/usr/bin/python3
"""
Defines MyList, a subclass of list, with additional functionality to
print sorted lists.
"""


class MyList(list):
    """
    MyList inherits from the built-in list class, adding a method to print
    the list sorted.
    """

    def print_sorted(self):
        """
        Prints the elements of the list sorted in ascending order without
        altering the original list.
        """
        print(sorted(self))
