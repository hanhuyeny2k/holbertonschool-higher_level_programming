#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None and a_dictionary is not {}:
        return max(a_dictionary.keys(), key=a_dictionary.get)
    else:
        return None
