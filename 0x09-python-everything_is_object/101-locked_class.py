#!/usr/bin/python3
"""locked class"""


class LockedClass:
    """
    A class that only allows creating an
    instance attribute with name 'first_name'
    """
    __slots__ = ['first_name']
