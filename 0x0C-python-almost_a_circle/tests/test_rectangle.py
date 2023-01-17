#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
"""Classes used to to test.\
        TestId\
"""

class TestId(unittest.TestCase):
    """Implementing"""
    def test_id(self):
        b = Rectangle(10, 2)
        self.assertEqual(b.id, 5)
        b2 = Rectangle(2, 10)
        self.assertEqual(b2.id, 6)
        b3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(b3.id, 12)
