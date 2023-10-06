#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        """ max at the end """
        self.assertEqual(max_integer([2, 4, 5]), 5)

        """ max at the beginning """
        self.assertEqual(max_integer([7, 2, 4, 5]), 7)

        """ max in the middle """
        self.assertEqual(max_integer([2, 4, 7, 6, 5]), 7)

if __name__ == '__main__':
    unittest.main()
