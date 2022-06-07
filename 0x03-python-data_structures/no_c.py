#!/usr/bin/python3
def no_c(my_string):
    n = len(my_string)
    for x in range(0, n):
        if ord(my_string[x]) == 'c' or ord(my_string[x]) == 'C':
            my_string.remove(x)


if __name__ == "__main__":
    no_c(my_string)
