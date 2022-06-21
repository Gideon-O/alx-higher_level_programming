#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints the integers in a list passed to it
    Returns the number of elements printed
    """
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (NameError):
            continue
    print()
    return printed
