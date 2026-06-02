#!/usr/bin/python3
"""
Module that defines a function to append a string
to a text file (UTF8) and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF8)
    and returns the number of characters added.

    Args:
        filename (str): name of the file
        text (str): text to append

    Returns:
        int: number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
