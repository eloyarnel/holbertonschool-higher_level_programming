#!/usr/bin/python3
"""
Module that defines a function that returns
the JSON representation of an object.
"""


import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: object to convert

    Returns:
        str: JSON representation of the object
    """
    return json.dumps(my_obj)
