#!/usr/bin/env python3
"""
Basic serialization module.
Provides functions to serialize a dictionary to a JSON file
and deserialize a JSON file back into a dictionary.
"""


import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The path/name of the output JSON file.
                        If the file already exists, it will be overwritten.
    """
    # Open the file in write mode ('w'). If the file exists, it gets replaced.
    # The 'with' statement ensures the file is properly closed after writing.
    with open(filename, 'w') as f:
        # json.dump() converts the Python dictionary to JSON format
        # and writes it directly to the file object 'f'
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize a JSON file back into a Python dictionary.

    Args:
        filename (str): The path/name of the input JSON file to read.

    Returns:
        dict: A Python dictionary containing the deserialized data from the JSON file.
    """
    # Open the file in read mode ('r') — the default mode
    # The 'with' statement ensures the file is properly closed after reading.
    with open(filename, 'r') as f:
        # json.load() reads the JSON data from the file object 'f'
        # and converts it back into a Python dictionary
        return json.load(f)
