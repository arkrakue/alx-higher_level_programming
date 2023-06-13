#!/usr/bin/python3
"""
    Contains a function that returns the list of
    attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.
    Args:
        obj: The object to inspect.
    Returns:
        A list of strings representing the names of the available
        attributes and methods of the object.
    """
    return dir(obj)
