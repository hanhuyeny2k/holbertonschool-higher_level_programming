#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestStringMethods(unittest.TestCase):

    def test_positive_integers(self):
        self.assertEqual(max_integer([1, 3, 5, 0]), 7)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)
