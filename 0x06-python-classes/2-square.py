#!/usr/bin/python3
"""Defines the size of the square"""


class Square:
    """Represents a square, creates a private instance attribute: size."""
    def __init__(self, size=0):
        """Initializing the size of the square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
