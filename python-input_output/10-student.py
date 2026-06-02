#!/usr/bin/python3
"""
Module that defines a Student class with JSON filtering.
"""


class Student:
    """
    Student class with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns the dictionary representation of the instance.

        If attrs is a list of strings, only attributes in that list
        are included. Otherwise, all attributes are returned.
        """
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

        return self.__dict__
