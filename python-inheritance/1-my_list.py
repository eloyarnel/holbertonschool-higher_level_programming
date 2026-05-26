#!/usr/bin/python3
"""Module that defines a custom list class"""


class MyList(list):
    """Custom list class that prints a sorted version of itself."""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
