#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    counter = 0
    for e in range(x):
        try:
            print(format(my_list[e]), end="")
            counter += 1
        except:
            break
    print()
    return counter
