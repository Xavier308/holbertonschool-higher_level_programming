#!/usr/bin/python3
"""
This module defines a class Student that represents a student and can
serialize to JSON and reload its attributes from a JSON dictionary.
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
        Filters attributes by attrs if it's a list of strings.

        Args:
            attrs (list, optional):
                List of strings representing the names of the
                attributes to retrieve.

        Returns:
            dict: A dictionary of the attributes of the instance.
        """
        # Check if attrs is properly formatted as a list of strings
        if isinstance(attrs, list):
            if all(isinstance(item, str) for item in attrs):
                filtered_attributes = {}
                for attribute_name in attrs:
                    if hasattr(self, attribute_name):
                        # Add attribute to the dictionary
                        value = getattr(self, attribute_name)
                        filtered_attributes[attribute_name] = value
                return filtered_attributes

        # Return all attributes if no valid 'attrs' provided
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance from a JSON dictionary.

        Args:
            json (dict):
                A dictionary with keys as attribute names and values as
                the attribute values.
        """
        for key, value in json.items():
            setattr(self, key, value)
