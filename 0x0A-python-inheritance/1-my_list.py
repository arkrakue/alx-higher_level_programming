#!/usr/bin/python3
"""
    Defines a class that inherits from a class
    list
"""


class MyList(list):
    """
        This class inherits from list and has a method
        to print the list in ascending order.
    """

    def print_sorted(self):
        """
            Prints list in order(ascending)
        """
        print(sorted(self))
