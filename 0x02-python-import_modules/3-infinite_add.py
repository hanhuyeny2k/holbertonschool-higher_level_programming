#!/usr/bin/python3
import sys
from add_0 import add
if __name__ == "__main__":
    argc = len(sys.argv)
    combine = 0
    if argc == 1:
        print("0")
    else:
        for i in range(1, argc):
            combine = combine + int(sys.argv[i])
    print("{}".format(combine))
