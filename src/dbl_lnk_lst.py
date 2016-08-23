# -*- coding: utf-8 -*-
"""Implementation of a dbl link-list data type in Python."""


class Node_Dll(object):

    def __init__(self, data, prev_node=None, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        if self.next_node is not None:
            return repr(self.data) + ', ' + repr(self.next_node)
        else:
            return repr(self.data)


class Dll(object):

    def __init__(self, params=None):
        """Initialize the linked list instance."""

        self.length = 0
        self.head = Node_Dll(None)
        self.tail = self.head
        self.head.data = None

        if hasattr(params, '__iter__'):
            for node in params:
                self.push(node)
        elif params:
            self.push(params)

    def __repr__(self):
        """Display the linked list."""
        try:
            return '(' + repr(self.head) + ')'
        except AttributeError:
            return '()'

    def __len__(self):
        return self.length

    def display(self):
        """
        Return a unicode string representing
        the list as if it were a Python tuple.
        """
        return '(' + repr(self.head) + ')'

    def push(self, val):
        """Insert the value val at the head of the list."""
        tmp = Node_Dll(val, None, None)

        if self.length == 0:
            self.head = tmp
            self.tail = tmp

        elif self.length >= 1:
            tmp.next_node = self.head
            self.head.prev_node = tmp
            self.head = tmp

        self.length += 1
        return self

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        if self.length > 1:
            popped_node = self.head
            self.head.next_node.prev_node = None
            self.head = self.head.next_node
            self.length -= 1
            return popped_node.data
        elif self.length == 1:
            popped_node_data = self.head.data
            self.head.data = None
            self.tail.data = None
            self.length = 0
            return popped_node_data
        else:
            return None

    def size(self):
        """Return the length of the list."""
        return self.length

    def search(self, val):
        """Return the node containing val in the list, if exists, else None."""
        current = self.head
        while current is not None:
            if current.data == val:
                return current
            current = current.next_node
        return None

    def remove(self, val):  # if last node --> set Node to None
        """Remove the given node from the list, wherever it might be."""
        node = self.search(val)

        if node.next_node is not None:
            node.data = node.next_node.data
            node.next_node = node.next_node.next_node
        elif node.next_node is None:
            self.tail = node.prev_node
            node.data = None
            node.prev_node.next_node = None

        self.length -= 1
        return self

    def append(self, val):
        """Append the val arg to the end of the list as a new node."""
        self.tail.next_node = Node_Dll(val, self.tail, None)
        self.tail = self.tail.next_node

    def shift(self):
        """
        Shift the node off the tail of the list and return the value of the
        node.
        """
        if self.length > 1:
            shifted_node = self.tail
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            self.length -= 1
            return shifted_node.data
        elif self.length == 1:
            shifted_node_data = self.tail.data
            self.head.data = None
            self.tail.data = None
            self.length = 0
            return shifted_node_data
        else:
            return None
