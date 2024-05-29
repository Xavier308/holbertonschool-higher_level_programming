#!/usr/bin/env python3
import csv
import json

""" This module contains a function that converts data from a CSV file to
    JSON format, handling serialization and file operations,
    and providing error feedback.
"""


def convert_csv_to_json(csv_filename):
    """
    Convert CSV data to JSON format.

    Parameters:
    csv_filename (str): The filename of the source CSV file.

    Returns:
    bool: True if the conversion was successful, False otherwise.
    """
    try:
        # Read data from CSV file using DictReader
        with open(csv_filename, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)  # Convert each row into a dictionary

        # Serialize the list of dictionaries to JSON and write to a file
        with open('data.json', 'w', newline='') as jsonfile:
            json.dump(data, jsonfile, indent=4)  # Pretty printing w indent

        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
