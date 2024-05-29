#!/usr/bin/python3
import pickle

"""
This module defines a CustomObject class capable of serializing its instances
to files using pickle and displaying its attributes.
"""


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the attributes of the object.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance of the object and save it to a file.

        Parameters:
        filename (str): The name of the file to save the serialized data.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            print(f"Failed to serialize object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Load and return an instance of CustomObject from a file.

        Parameters:
        filename (str): The name of the file from which to load the object.

        Returns:
        CustomObject: The deserialized object, or None if an error occurs.
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Failed to deserialize object: {e}")
            return None
