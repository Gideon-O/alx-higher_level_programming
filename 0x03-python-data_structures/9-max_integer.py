#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if n <= 0:
        return None
    else:
        max_el = my_list[0]
        for i in my_list:
            if max_el < my_list[i]:
                max_el = my_list[i]
        return max_el


if __name__ == "__main__":
    max_integer(my_list)
