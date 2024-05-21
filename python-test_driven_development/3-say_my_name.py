#!/usr/bin/python3
"""This module provides the function say_my_name which prints a person's name.
   It handles basic input validation in a straightforward manner.
"""


def say_my_name(first_name, last_name=""):
    """Prints a full name in the format 'My name is <first name> <last name>'.

    Args:
        first_name (str): The first name of the person.
        last_name (str): The last name of the person;
        defaults to an empty string.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    Returns:
        None: This function prints directly to standard output.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
