#!/usr/bin/python3
"""Square Class"""


class Square:
    """Square class with its size"""

    def __init__(self, size=0):
        """ Square Object

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    self.__size = size
