#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    combine = 0
    if argc == 1:
        print("{}".format(combine))
        exit(0)
    else:
        for i in range(1, argc):
            combine = combine + int(sys.argv[i])
    print("{}".format(combine))
