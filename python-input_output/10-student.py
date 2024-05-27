#!/usr/bin/python3
"""
This module defines a class Student that represents a student with
customizable JSON serialization.
"""


class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        Filters the dictionary by attrs if it's a list of strings.

        Args:
            attrs (list, optional): The list of attribute names to include
            in the result.

        Returns:
            dict: A dictionary containing the specified attributes of the
            instance, or all attributes if attrs is None or not a list of
            strings.
        """

        is_attrs_list_of_strings = (
            isinstance(attrs, list) and
            all(isinstance(item, str) for item in attrs)
        )

        if is_attrs_list_of_strings:
            filtered_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    filtered_dict[key] = getattr(self, key)
            return filtered_dict
        else:
            return self.__dict__
