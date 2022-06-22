#!/usr/bin/python3
"""
@Author: Gideon Osoro
ALX School
"""


class Square:
    """
    Square class definition
    Attribute - size(private)
    """
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
