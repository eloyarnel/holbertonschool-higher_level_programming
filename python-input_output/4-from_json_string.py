#!/usr/bin/python3
"""
Module that defines a function that returns
a Python object represented by a JSON string.
"""
import json

def from_json_string(my_str):
    """
    Returns a Python data structure represented
    by a JSON string.

    Args:
        my_str (str): JSON string

    Returns:
        object: Python representation of the JSON string
    """
    return json.loads(my_str)
