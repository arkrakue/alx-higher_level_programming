#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Returns the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Creates a json representation of an object
    Arguments:
        obj (obj): The object inputted to create a class
    Return:
        A jason representation
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
