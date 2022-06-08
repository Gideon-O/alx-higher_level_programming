#!/usr/bin/python3
def search_replace(my_list, search, replace):
    for x in my_list:
        map(lambda search, replace: x = replace if x == search)
    return (my_list)
