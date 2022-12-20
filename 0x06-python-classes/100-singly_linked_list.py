#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        if type(data) != int:
            raise Exception("data must be integer")
        elif next_node == None:
            raise Exception("next_node must be a Node object")
        elif next_node != None or type(data) == int:
            self.data = data
            self.next_node = next_node


    def data(self):
        return self.data


    def data(self, value):
        if type(data) != int:
            raise Exception("data must be an integer")
        else:
            self.data = value


    def next_node(self):
        return self.next_node


    def next_node(self, value):
        if value == None:
            raise Exception("next_node must be an Node Object")
        else:
            self.next_node = value



class SinglyLinkedList:
    def __init__(self):
        self.head = []


    def sorted_insert(self, value):
        self.head.append(value)
        self.sort = sorted(self.head)
        print(*self.sort)
