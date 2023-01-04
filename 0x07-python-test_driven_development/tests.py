#!/usr/bin/python3
from add_integer import add_integer
import unittest

class Test(unittest.TestCase):
    def testing(self):
        self.assertRaises(TypeError, add_integer, "a must be an integer")
        #self.assertEqual(formatted, "a must be an integer")
