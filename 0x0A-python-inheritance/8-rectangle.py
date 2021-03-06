#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Defines a Rectangle using BaseGeometry module"""


class Rectangle(BaseGeometry):
    """Represent a Rectangle."""
    def __init__(self, width, height):
        """Initializing the width and height."""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
