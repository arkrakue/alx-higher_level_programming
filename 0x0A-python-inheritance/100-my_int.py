##!/usr/bin/python3
"""
    Creates a class MyInt that inherits from int
"""


class MyInt(int):
    """
        Class MyInt that inherits from int,
        has the == and != operators inverted
    """

    def __eq__(self, other):
        """
            Return boolean if the self and other are equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
            Return boolean if the self and other are equal
        """
        return super().__eq__(other)
