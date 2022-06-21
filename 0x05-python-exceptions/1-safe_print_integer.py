#!/usr/bin/python3
def safe_print_integer(value):
    """
    Function that prints an integer value
    Returns: True if integer is printed, 
             False if error occurs
    """
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        return False
