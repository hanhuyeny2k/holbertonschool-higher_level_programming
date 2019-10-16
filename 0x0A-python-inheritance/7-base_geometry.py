#!/usr/bin/python3
"""Define BaseGeometry class"""

class BaseGeometry:
    """Defines BaseGeometry."""
    def area(self):
        """Raise an Exception with a message."""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """Validates value."""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
