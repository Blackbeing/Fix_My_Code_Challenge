#!/usr/bin/python3
"""This module defines a class square"""


class square:
    """
    A class representing a square.

    Attributes:
    - width (float): The width of the square.
    - height (float): The height of the square.
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initialize the Square instance.

        Parameters:
        - *args: Variable positional arguments.
        - **kwargs: Variable keyword arguments.
        """

        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """
        Calculate the area of the square.

        Returns:
        float: The area of the square.
        """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """
        Calculate the perimeter of the square.

        Returns:
        float: The perimeter of the square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Return a string representation of the Square instance.

        Returns:
        str: A string in the format "{width}/{height}".
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
