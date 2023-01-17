#!/usr/bin/python3

import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
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

class ToJsonString(unittest.TestCase):
    """Implementing"""
    def to_j_str(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dict = Base.to_json_string([dictionary])
        captured = io.StringIO()
        sys.stdout = captured
        print(dictionary)
        self.assertEqual(captured.getvalues()[:-1], "{'x': 2, 'width': 10, 'id': 10, 'height': 7, 'y': 8}")
        captured = io.StringIO()
        sys.stdout = captured
        print(json_dict)
        self.assertEqual(captured.getvalues()[:-1], '{"x": 2, "width": 10, "id": 10, "height": 7, "y": 8}')
        dictionary = []
        json_dict = Base.to_json_string([dictionary])
        captured = io.StringIO()
        sys.stdout = captured
        print(dictionary)
        self.assertEqual(captured.getvalues()[:-1], '[]')
        captured = io.StringIO()
        sys.stdout = captured
        print(json_dict)
        self.assertEqual(captured.getvalues()[:-1], "[]")
