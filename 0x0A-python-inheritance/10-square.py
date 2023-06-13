#!/usr/bin/python3
"""
Creates class Square that inherits Rectangle
and takes argument: size.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class Square that inherits Rectangle and takes argument: size.
    """
    def __init__(self, size):
        """
        Initializes a new Square object with the given size.
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
