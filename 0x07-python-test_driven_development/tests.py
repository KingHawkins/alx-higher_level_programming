#!/usr/bin/python3
import unittest
add_integer = __import__('0-add_integer').add_integer

class Test(unittest.TestCase):
    def testing(self):
        self.assertRaises(TypeError, add_integer, "a must be an integer")
        #self.assertEqual(formatted, "a must be an integer")
