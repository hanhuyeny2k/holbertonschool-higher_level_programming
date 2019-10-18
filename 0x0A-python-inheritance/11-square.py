#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""class Square inherits from Rectangle"""


class Square(Rectangle):
    """Represent a class Square"""
    def __init__(self, size):
        """Initialize the size of the Square"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Returns the Square area."""
        return self.__size * self.__size

    def __str__(self):
        """Print the Square width by height."""
        return ("[Square] {}/{}".format(self.__size, self.__size))
