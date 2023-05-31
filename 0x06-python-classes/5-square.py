#!/usr/bin/python3
"""Square class"""


class Square:
    """Square class with size"""

    def __init__(self, size=0):
        """square object"""
        self.size = size

    @property
    def size(self):
        """Getter method for size property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size property"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using the # character"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
