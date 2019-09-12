#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
if __name__ == "__main__":
    a = 10
    b = 5
    to_add = add(a, b)
    to_sub = sub(a, b)
    to_mul = mul(a, b)
    to_div = div(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, to_add))
    print("{:d} - {:d} = {:d}".format(a, b, to_sub))
    print("{:d} * {:d} = {:d}".format(a, b, to_mul))
    print("{:d} / {:d} = {:d}".format(a, b, to_div))
