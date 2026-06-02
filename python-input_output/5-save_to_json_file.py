#!/usr/bin/python3
"""
Module that defines a function that writes
a Python object to a text file using JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: Python object to serialize
        filename (str): name of the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
