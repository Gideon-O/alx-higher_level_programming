#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    int y = 0

    try:
        for y = 0, i in my_list:
            print("{}".format(i), end="")
            y++;
        return (y)
    except:
        print("An error occured")
