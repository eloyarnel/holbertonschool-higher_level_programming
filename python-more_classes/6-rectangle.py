#!/usr/bin/python3
"""Defines a rectangle"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width with validation"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height with validation"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Return rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """Draw rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""

        rows = []
        for _ in range(self.height):
            rows.append("#" * self.width)
        return "\n".join(rows)

    def __repr__(self):
        """Representation to recreate object"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Destructor message and instance counter"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
