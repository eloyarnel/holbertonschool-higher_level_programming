#!/usr/bin/python3
"""Module that defines a Square class with size property."""

class Square:
    """Defines a square by size"""

    def __init__(self, size=0):
        """Initializes the square

        Args:
            size (int): The size of the square
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value (int): The new size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
