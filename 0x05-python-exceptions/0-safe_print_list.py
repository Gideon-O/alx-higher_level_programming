#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Prints the elements of a list
    Returns the number of elements printed
    """
    int y = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            y += 1
        except:
            continue
    print()
    return y
