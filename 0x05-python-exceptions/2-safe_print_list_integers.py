#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Function to print only integers in a list
    Returns the number of integers printed
    """
    int_printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]))
            int_printed += 1
        except (ValueError, TypeError):
            continue
    print()
    return int_printed
