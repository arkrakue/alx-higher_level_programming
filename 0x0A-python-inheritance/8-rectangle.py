#!/usr/bin/python3
"""
    Creates class Rectangle that inherits BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Class Rectangle that inherits
        BaseGeometry and takes two arguments: width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with the given width and height.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
