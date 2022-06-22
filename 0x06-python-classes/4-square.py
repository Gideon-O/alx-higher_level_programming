#!/usr/bin/python3
"""
@Author - Gideon Osoro
ALX School
"""


class Square:
    """
    Square class definition
    Has the 'getter' and 'setter' concepts covered
    """
    def __init__(self, seize=o):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area
