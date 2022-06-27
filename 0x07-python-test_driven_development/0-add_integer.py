#!/usr/bin/python3
'''
@Author - Gideon Osoro
ALX Shool tasks
'''


def add_integer(a, b=98):
    '''
    A function that adds only to integers
    Parameters: a, b
    b initialized to 98
    returns the sum of the two integers, if no error occurs
    '''
    if type(a) is not int:
        if type(a) is float and a == a and abs(a) <= 1.7976931348623158e+308:
            a = int(a)
        else:
            raise TypeError("a must be integer")
    if type(b) is not int:
        if type(b) is float and b == b and abs(b) <= 1.7976931348623158e+308:
            b = int(b)
        else:
            raise TypeError("b must be integer")
    return a + b
