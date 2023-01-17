#!/usr/bin/python3

import unittest
from models.base import Base
"""Classes used to to test.\
        TestId\
"""

class TestId(unittest.TestCase):
    """Implementing"""
    def test_id(self):
        b = Base()
        self.assertEqual(b.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base()
        self.assertEqual(b3.id, 3)
        b4 = Base()
        self.assertEqual(b4.id, 4)
        b = Base(12)
        self.assertEqual(b.id, 12)
