#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    n = len(my_list)
    if idx < 0:
        return my_list
    elif idx > n:
        return my_list
    else:
        my_list.insert(idx, element)
        my_list.remove(idx + 1)
        return my_list

if __name__ == "__main__":
  replace_in_list(my_list, idx, element)
