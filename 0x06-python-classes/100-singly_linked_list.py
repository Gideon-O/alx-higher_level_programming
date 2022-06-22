#!/usr/bin/python3
"""
@Author - Gideon Osoro
ALX Shool
"""


class Node:
    """
    Node class for a singly linked list
    Attribute - Data and Nect node pointer
    """
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    def data(self, value):
        """
        Sets the data node
        Raises an exception is data is not integer
        """
        if type(data) is int:
            self.__data = data
        if type(data) is not int:
            raise TypeError("data must be an integer")

    def data(self):
        return self.__data

    def next_node(self, value):
        """
        Sets the pointer to next node
        Raises an exception if value is not None or Node Object
        """
        self.__next_node = next_node
        if value is not None or value is not Node:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """
    Singly linked list class
    """
    def __init__(self, head):
        self.__head = head

    def sorted_insert(self, value):
        self.__value = value
        return SinglyLinkedList.sort()
