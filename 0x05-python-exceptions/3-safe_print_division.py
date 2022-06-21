#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Function to multuply two integers
    Returns the value of the division, otherwise returns None
    """
    div_int = None
    try:
        div_int = a / b
        return div_int
    except (ZeroDivisionError, ValueError):
        return div_int
    finally:
        print("Inside Result: {:d}".format(div_int))
