#!/usr/bin/python3
"""
    Checks the instance of an object of a specified class
"""


def is_same_class(obj, a_class):
    """
        Determine wheather an object is an instance
        of a class
        Args:
            obj: The object to check
            a_class: The class to check with
        Returns:
            True for an instance and False otherwise
    """
    return (type(obj) == a_class)
