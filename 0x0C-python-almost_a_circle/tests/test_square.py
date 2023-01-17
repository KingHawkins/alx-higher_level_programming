#!/usr/bin/python3

import unittest
import sys
import io
from models.square import Square
"""Classes used to to test.\
        TestId\
"""

class TestArea(unittest.TestCase):
    """Implementing"""
    def test_area(self):
        b = Square(5)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(b)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (14) 0/0 - 5')
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(b.area())
        self.assertEqual(capturedOutput.getvalue()[:-1], '25')
        b3 = Square(2, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(b3)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (15) 2/0 - 2')
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(b3.area())
        self.assertEqual(capturedOutput.getvalue()[:-1], '4')
        b4 = Square(3, 1, 3)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(b4)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (16) 1/3 - 3')
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(b4.area())
        self.assertEqual(capturedOutput.getvalue()[:-1], '9')

class TestValues(unittest.TestCase):
    """checks if there will be a an exception raised"""
    def test_values(self):
        with self.assertRaises(TypeError):
            Square('9')
        with self.assertRaises(ValueError):
            Square(-10)
        with self.assertRaises(TypeError):
            Square({})

class TestObjRepresentation(unittest.TestCase):
    """tests for obj representation"""
    def test_obj_representation(self):
        r1 = Square(6)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (17) 0/0 - 6')
        r2 = Square(1)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r2)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (18) 0/0 - 1')

class TestUpdate(unittest.TestCase):
    """tests if rectangle class is updated"""
    def test_update(self):
        r1 = Square(5)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (19) 0/0 - 5')
        r1.update(10)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (10) 0/0 - 5')
        r1.update(1, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (1) 0/0 - 2')
        r1.update(1, 2, 3)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (1) 3/0 - 2')
        r1.update(1, 2, 3, 4)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (1) 3/4 - 2')
        r1.update(x=12)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (1) 12/4 - 2')
        r1.update(size=7, y=1)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (1) 12/1 - 7')
        r1.update(size=7, id=89, y=1)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Square] (89) 12/1 - 7')

class TestDictionary(unittest.TestCase):
    """tests for dictionary conversion"""
    def to_dictionary(self):
        s2 = Square(10, 2, 1)
        s2_dictionary = s2.to_dictionary()
        captured = io.StringIO()
        sys.stdout = captured
        print(s2_dictionary)
        self.assertEqual(captured.getvalue()[:-1], "{'id': 9, 'x': 2, 'size': 20, 'y': 1}")
