#!/usr/bin/python3
"""
Returns a python object represented
by a JSON string
"""
import json


def from_json_string(my_str):
    """
    Convert a json string to a python object
    Arguments:
        my_obj (str): The inputed object to convert in json format
    Return:
        A Python object from json
    """
    return json.loads(my_str)
