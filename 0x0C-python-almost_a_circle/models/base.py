#!/usr/bin/python3
'''
Creates a Base class 
'''
import json


class Base:
    '''
    class Base with private attribute __init__.py

    Args:
        id: public instance value
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
