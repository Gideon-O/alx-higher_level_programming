#!/usr/bin/python3
"""
@Author: Gideon Osoro
ALX School
"""


class Square:
    """
    Square class definition and instatiation
    Attributes - size
    Method - area
    """
    def __init__(self, size=0):
        size.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(size):
        return size * size
