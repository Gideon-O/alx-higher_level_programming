#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return (None)
    for key, value in a_dictionary.items():
        return (key if max(a_dictionary.values())
