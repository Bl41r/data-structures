"""Implementation of a link-list data type in Python."""


class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList(object):

    def __init__(self, node_list):
        self.node_list = node_list
