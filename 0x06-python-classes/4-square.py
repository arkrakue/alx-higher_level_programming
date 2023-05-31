#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class with its size"""

    def __init__(self, size=0):
        """Square object

        Args:
            size (int): The size of the new square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.size = size

    @property
    def size(self):
        """Get size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set  size of the square

        Args:
            value (int): The new size of the square

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the current square area"""
        return self.__size ** 2
