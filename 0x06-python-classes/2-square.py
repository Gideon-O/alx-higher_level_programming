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
        try:
            size.__size = size
        except TypeError:
            print("size must be an integer")
