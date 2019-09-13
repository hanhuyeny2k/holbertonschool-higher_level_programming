#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
if __name__ == "__main__":
    argc = len(sys.argv)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif sys.argv[2] not in '+-*/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    elif sys.argv[2] == '+':
        to_add = add(a, b)
        print("{:d} + {:d} = {:d}".format(a, b, to_add))
    elif sys.argv[2] == '-':
        to_sub = add(a, b)
        print("{:d} - {:d} = {:d}".format(a, b, to_sub))
    elif sys.argv[2] == '*':
        to_mul = add(a, b)
        print("{:d} * {:d} = {:d}".format(a, b, to_mul))
    elif sys.argv[2] == '/':
        to_div = add(a, b)
        print("{:d} / {:d} = {:d}".format(a, b, to_div))
