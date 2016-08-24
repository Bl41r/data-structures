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

        self.head = None
        self.tail = None

        try:
            for node in params:
                self.push(node)
        except TypeError:
            if params is not None:
                raise TypeError('Argument is not iterable.  Must use an iterable type to initialize Dll.')

    def __repr__(self):
        """Display the linked list."""
        return '(' + repr(self.head) + ')'

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

        if self.size() == 0:
            self.head = tmp
            self.tail = tmp

        elif self.size() >= 1:
            tmp.next_node = self.head
            self.head.prev_node = tmp
            self.head = tmp

        return self

    def pop(self):
        """Pop the first value off the head of the list and return it."""

        try:
            popped_val = self.head.data
        except AttributeError:
            raise IndexError('Cannot pop an empty list.')

        try:
            self.head.next_node.prev_node = None
        except AttributeError:
            pass
        self.head = self.head.next_node
        return popped_val

    def size(self):
        """Return the length of the list."""
        current = self.head
        inc = 0
        while True:
            try:
                current = current.next_node
            except AttributeError:
                return inc
            inc += 1

    def search(self, val):
        """Return the node containing val in the list, if exists, else None."""
        current = self.head
        while current is not None:
            try:
                if current.data == val:
                    return current
            except AttributeError:
                    break
            current = current.next_node
        return None

    def remove(self, val):  # if last node --> set Node to None
        """Remove the given node from the list, wherever it might be."""
        node = self.search(val)
        if node is None:
            raise ValueError('Value not in list.')
        try:
            node.prev_node.next_node = node.next_node
        except AttributeError:
            self.head = node.next_node
        try:
            node.next_node.prev_node = node.prev_node
        except AttributeError:
            self.tail = node.prev_node

    def append(self, val):
        """Append the val arg to the end of the list as a new node."""
        tmp = Node_Dll(val, self.tail, None)
        try:
            self.tail.next_node = tmp
            self.tail = self.tail.next_node
        except AttributeError:
            self.push(tmp.data)
        return self

    def shift(self):
        """
        Shift the node off the tail of the list and return the value of the
        node.
        """
        try:
            shift_val = self.tail.data
        except AttributeError:
            raise IndexError('Cannot shift an empty list.')

        try:
            self.tail.prev_node.next_node = None
        except AttributeError:
            self.head = None

        self.tail = self.tail.prev_node
        return shift_val
