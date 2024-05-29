#!/usr/bin/python3
import xml.etree.ElementTree as ET

"""
This module provides functions to serialize a Python dictionary into XML
format and save it to a file, and to deserialize XML back into a
dictionary, utilizing Python's xml.etree.ElementTree.
"""


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into XML format and save it to a file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the XML.

    Returns:
    None
    """
    root = ET.Element("data")  # Create the root element
    for key, value in dictionary.items():
        # Create a child element for each dictionary entry
        child = ET.SubElement(root, key)
        # Set the text of each child as the string representation of the value
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)  # Write the XML to a file
    print(f"Dictionary serialized to {filename}")


def deserialize_from_xml(filename):
    """
    Read XML data from a file and return a deserialized Python dictionary.

    Parameters:
    filename (str): The name of the file from which to read the XML.

    Returns:
    dict: A dictionary representing the deserialized XML data.
    """
    tree = ET.parse(filename)  # Parse the XML file
    root = tree.getroot()
    result_dict = {}
    for child in root:
        # Convert each element back into dictionary key-value pairs
        result_dict[child.tag] = child.text

    return result_dict
