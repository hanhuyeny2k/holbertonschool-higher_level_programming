#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argc = len(sys.argv) - 1
    if argc == 0:
        print("{:d} arguments.".format(argc))
    elif argc == 1:
        print("{:d} argument:".format(argc))
        print("{:d}: {}".format(argc, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argc))
        for i in range(1, argc+1):
            print("{:d}: {}".format(i, sys.argv[i]))
