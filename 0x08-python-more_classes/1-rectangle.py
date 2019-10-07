#!/usr/bin/python3
"""Defines a rectangle."""


class Rectangle:
    """Defines a rectangle by its width and height."""
    @property
    def width(self):
        """Create a getter to retrieve the data."""
        return self.__width

    @width.setter
    def width(self, value):
        """Create a setter to protect data and set it."""
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Create a getter to retrieve the data."""
        return self.__height

    @height.setter
    def height(self, value):
        """Create a setter to protect data and set it."""
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        """Initializing width and height of a rectangle."""
        self.width = width
        self.height = height
