#!/usr/bin/python3

"""Define class Node."""

class Node:
    """Represent class node."""
    def __init__(self, data, next_node=None):
        """Initialize node data
        Args:
            data(int): data to be stored in linked list
            next_node(None): initialize linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data"""
        return self.__data

    @data.setter
    def data(self, value):
        if(not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if(not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Define class SinglyLinkedList."""
class SinglyLinkedList:
"""represent class singlyLinkedlist."""
    __head = None

    def __init__(self):
        """
            Represent object."""
        pass

    def __str__(self):
        """
        Initialize linked list
        """
        newList = []
        while(self.__head):
            newList.append(self.__head.data)
            self.__head = self.__head.next_node
"""Returns new list"""
        return("\n".join([str(x) for x in sorted(newList)]))

    def sorted_insert(self, value):
"""Instantiates node object."""
        newNode = Node(value, self.__head)
        self.__head = newNode
