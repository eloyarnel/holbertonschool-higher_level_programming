#!/usr/bin/python3
"""Module to check if obj inherits from a_class."""


def inherits_from(obj, a_class):
    """Return True if obj inherits from a_class (not exact class)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
