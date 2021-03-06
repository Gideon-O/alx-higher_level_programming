#!/usr/bin/python3
"""
@Author - Gideon Osoro
ALX School
"""


class Square:
    """
    Square class definition
    Has the 'getter' and 'setter' concepts covered
    Recursively prints the square with '#'
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
