"""Implementation of a link-list data type in Python."""


class Node(object):

    def __init__(self, data, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        if next_node is not None:
            self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        try:
            return str(self.data) + u', ' + str(self.next_node)
        except AttributeError:
            return str(self.data)


class LinkedList(object):

    def __init__(self, params=None):
        """Initialize the linked list instance."""

        self.head = None
        self.length = 0

        try:
            for node in params:
                self.length += 1
                self.push(node)
        except TypeError:
            self.push(params)
            self.length = 1

    def __repr__(self):
        """Display the linked list."""
        return u'(' + str(self.head) + u')'

    def __len__(self):
        return self.length

    def display(self):
        """Return a unicode string representing the list as if it were a Python tuple."""
        return u'(' + str(self.head) + u')'

    def push(self, val):
        """Insert the value val at the head of the list."""
        if self.head is not None:
            self.head = Node(val, self.head)
            self.length += 1
        else:
            self.head = Node(val)
            self.length += 1

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        if self.length > 0:
            popped_node = self.head
            self.head = self.head.next_node
            self.length -= 1
            return popped_node.data
        else:
            return None

    def size(self):
        """Return the length of the list."""
        return self.length

    def search(self, val):
        """Return the node containing val in the list, if exists, else None."""
        current = self.head
        while current.data is not None:
            if current.data == val:
                return current
            elif current.next_node is None:
                return None
            current = current.next_node

    def remove(self, node):
        """Remove the given node from the list, wherever it might be."""
        node.data = node.next_node.data
        node.next_node = node.next_node.next_node
