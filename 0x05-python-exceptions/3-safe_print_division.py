#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Function to multuply two integers
    Returns the value of the division, otherwise returns None
    """
    try:
        div_int = a / b 
    except (ZeroDivisionError):
        div_int = None
    finally:
        print("Inside Result: {:d}".format(div_int))
    return div_int
