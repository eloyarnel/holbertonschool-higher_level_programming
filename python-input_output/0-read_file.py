#!/usr/bin/python3
"""
Module that defines a function to read a text file
and print its contents to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its contents to stdout.

    Args:
        filename (str): name of the file to read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
