#!/usr/bin/python3
"""Module that defines a Square class."""

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes the data."""

        # Check if size is NOT an integer
        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        # Check if size is negative
        if size < 0:
            raise ValueError("size must be >= 0")

        # Store the validated size value
        self.__size = size
