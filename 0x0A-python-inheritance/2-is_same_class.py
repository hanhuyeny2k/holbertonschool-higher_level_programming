#!/usr/bin/python3


def is_same_class(obj, a_class):
    """Return True if the object is exactly an instance of the specified
        class"""
    return type(obj) == a_class
