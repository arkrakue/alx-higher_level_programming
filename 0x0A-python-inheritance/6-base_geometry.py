#!/usr/bin/python3
"""
    Creates defines a class named BaseGeometry with
    public instance method area that raises an exception.
"""


class BaseGeometry:
    """
        A class named BaseGeometry with a public
        instance method area that raises an exception.
    """
    def area(self):
        """
            Raises an Exception with the message
            "area() is not implemented".
        """
        raise Exception("area() is not implemented")
