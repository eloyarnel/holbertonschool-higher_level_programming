#!/usr/bin/python3
"""Module defining is_same_class function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class."""
    return type(obj) is a_class
