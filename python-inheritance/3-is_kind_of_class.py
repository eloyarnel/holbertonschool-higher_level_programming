#!/usr/bin/python3
"""Module to check instance or inherited class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or inherited class."""
    return isinstance(obj, a_class)
