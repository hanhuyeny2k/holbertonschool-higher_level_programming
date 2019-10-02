#!/usr/bin/python3
"""Defines the size of the square."""


class Square:
    """Represents a square, creates a private instance attribute: size."""
    @property
    def size(self):
        """Create a getter to protect and reserve the data."""
        return self.__size

    @size.setter
    def size(self, value):
        """Create a setter to protect putting bad data inside a square."""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __init__(self, size=0):
        """Initializing the size of the square."""
        self.__size = size

    def area(self):
        """Return the area of a square."""
        return(self.__size * self.__size)
