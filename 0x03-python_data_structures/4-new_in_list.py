#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    return my_list.insert(idx, element).remove(idx + 1)


if __name__ == "__main__":
    new_in_list(my_list, idx, element)
