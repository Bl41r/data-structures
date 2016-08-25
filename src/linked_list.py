"""Implementation of a link-list data type in Python."""

from __future__ import unicode_literals


class Node(object):
    """Node class with data and next_node pointer.  Init with value."""

    def __init__(self, data, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        if self.next_node is not None:
            return repr(self.data) + ', ' + repr(self.next_node)
        else:
            return repr(self.data)


class LinkedList(object):
    """Linked List data structure.  Takes in an iterable."""

    def __init__(self, params=None):
        """Initialize the linked list instance."""
        self.head = None

        try:
            for value in params:
                self.push(value)
        except TypeError:
            if params is not None:
                raise TypeError('This function requires an iterable value')

    def __repr__(self):
        """Display the linked list."""
        return '(' + repr(self.head) + ')'

    def __len__(self):
        """Return length of list."""
        return self.size()

    def display(self):
        """Return a unicode string representing the list as if it were a Python tuple."""
        return '(' + repr(self.head) + ')'

    def push(self, val):
        """Insert the value val at the head of the list."""
        self.head = Node(val, self.head)

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        popped_node = self.head
        try:
            self.head = self.head.next_node
            return popped_node.data
        except AttributeError:
            pass
            return None

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
            if current.data == val:
                break
            current = current.next_node
        return current

    def remove(self, node):
        """Remove the given node from the list, from any point in the list."""
        parent = self.head
        if parent.next_node == node.next_node:
            self.head = parent.next_node
            parent.next_node = None
            return

        while parent.next_node != node:
            parent = parent.next_node

        try:
            parent.next_node = parent.next_node.next_node
        except AttributeError:
            parent.next_node = None
