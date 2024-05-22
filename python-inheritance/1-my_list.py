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

if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
