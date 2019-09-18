#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if sentence == ():
        sentence[0] = None
    for i in sentence:
        return length, first
