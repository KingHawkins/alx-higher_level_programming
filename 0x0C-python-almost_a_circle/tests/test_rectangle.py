#!/usr/bin/python3

import unittest
import sys
import io
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

class TestValues(unittest.TestCase):
    """checks if there will be a an exception raised"""
    def test_values(self):
        with self.assertRaises(TypeError):
            Rectangle(10, '2')
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, {})
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 3, -1)

class TestObjRepresentation(unittest.TestCase):
    """tests for obj representation"""
    def test_obj_representation(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (12) 2/1 - 4/6')
        r2 = Rectangle(5, 5, 1)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r2)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (7) 1/0 - 5/5')

class TestUpdate(unittest.TestCase):
    """tests if rectangle class is updated"""
    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (8) 10/10 - 10/10')
        r1.update(89)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (89) 10/10 - 10/10')
        r1.update(89, 2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (89) 10/10 - 2/10')
        r1.update(89, 2, 3)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (89) 10/10 - 2/3')
        r1.update(89, 2, 3, 4)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (89) 4/10 - 2/3')
        r1.update(89, 2, 3, 4, 5)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (89) 4/5 - 2/3')

class TestUpdateTwo(unittest.TestCase):
    """tests if rectangle class is updated"""
    def test_update_two(self):
        r1 = Rectangle(10, 10, 10, 10)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (9) 10/10 - 10/10')
        r1.update(height=1)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (9) 10/10 - 10/1')
        r1.update(width=1, x=2)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (9) 2/10 - 1/1')
        r1.update(y=1, width=2, x=3, id=89)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (89) 3/1 - 2/1')
        r1.update(x=1, height=2, y=3, width=4)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(r1)
        self.assertEqual(capturedOutput.getvalue()[:-1], '[Rectangle] (89) 1/3 - 4/2')
