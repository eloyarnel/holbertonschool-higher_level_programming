#!/usr/bin/python3
"""
Module that defines a function to return the dictionary
description of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structures
    for JSON serialization of an object.

    Args:
        obj: instance of a class

    Returns:
        dict: dictionary description of obj
    """
    return obj.__dict__
