#!/usr/bin/python3
def safe_print_integer_err(value):
    """
    A function to print integers
    Returns True if value is integer
    Returns False if value is not integer and
    prints error message in 'stderr'
    """
    try:
        print("{:d}".format(value))
        return True
    except TypeError:
        print("Exception: Not an integer", file=sys.stderr)
        return False
