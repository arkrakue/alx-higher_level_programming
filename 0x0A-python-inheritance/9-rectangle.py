#!/usr/bin/python3
"""
Creates classRectangle that inherits from BaseGeometry
and takes two arguments: width and height.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Class Rectangle that inherits from BaseGeometry and
    takes two arguments: width and height.
    """
    def __init__(self, width, height):
        """
        Initializes a new Rectangle object with the given width and height.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
