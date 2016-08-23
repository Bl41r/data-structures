"""Implementation of a linked-list data type in Python."""


class Node(object):

    def __init__(self, data, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        if self.next_node:
            return str(self.data) + u', ' + str(self.next_node)
        else:
            return str(self.data)


class LinkedList(object):

    def __init__(self, params=None):
        """Initialize the linked list instance."""

        self.head = Node(None)
        self.head.data = None
        self.length = 0

        try:
            for node in params:
                self.push(node)
        except TypeError:
            print('argument is not iterable.')

    def __repr__(self):
        """Display the linked list."""
        return u'(' + str(self.head) + u')'

    def __len__(self):
        return self.length

    def display(self):
        """Return a unicode string representing the linked list as if it were a Python tuple."""
        return u'(' + str(self.head) + u')'

    def push(self, val):
        """Insert a node with val at the head of the list."""
        self.head = Node(val, self.head)
        self.length += 1
        return self

    def pop(self):
        """Pop the first value off the head of the linked list and return it."""
        if self.length > 0:
            popped_node = self.head
            self.head = self.head.next_node
            self.length -= 1
            return popped_node.data
        else:
            raise IndexError('Cannot pop an empty list.')

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
        raise ValueError("That value does not exist in this list.")

    def remove(self, node):
        """Remove the given node from the list, wherever it might be."""
        try:
            if node.next_node is not None:
                node.data = node.next_node.data
                node.next_node = node.next_node.next_node
            else:   # if last node in list
                node.data = None
                node.next_node = None
        except AttributeError:
            pass

        self.length -= 1
        return self
