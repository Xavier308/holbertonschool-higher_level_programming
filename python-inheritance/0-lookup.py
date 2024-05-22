#!/usr/bin/python3
"""
Provides 'lookup' function to list object attributes and methods.
Useful for debugging and introspection of Python objects.
No external modules required.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj (any): The object to look up attributes and methods for.

    Returns:
        list: A list of strings, each string being an attribute or
        method name.
    """
    return dir(obj)

if __name__ == "__main__":
    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
