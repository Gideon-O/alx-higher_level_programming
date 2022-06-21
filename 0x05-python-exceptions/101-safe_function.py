#!/usr/bin/python3
def safe_function(fct, *args):
    """
    A function that executes a function
    Returns the result of the executed function
    """
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
