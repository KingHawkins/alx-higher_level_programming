#!/usr/bin/python3

"""inheriting from a parent class"""


class MyList(list):
    """Implementation"""
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints sorted list items"""
        print(sorted(self.copy()))
