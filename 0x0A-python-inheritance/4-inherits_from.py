#!/usr/bin/python3
"""
    Checks the instance of an object of a class that inherited
    from
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        A boolean indicating whether the object is an instance of a class
        that inherited (directly or indirectly) from the specified class.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
