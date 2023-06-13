#!/usr/bin/python3
"""
    Checks if an object is an instance of a class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from,
    the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        A boolean indicating whether the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class.
    """
    return isinstance(obj, a_class)
