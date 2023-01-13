#!/usr/bin/python3

"""inherits from integer"""


class MyInt(int):
    """implementing"""
    def __eq__(self, other):
        """inverts equality sign"""
        return int.__ne__(self, other)


    def __ne__(self, other):
        """inverts not equal sign"""
        return int.__eq__(self, other)
