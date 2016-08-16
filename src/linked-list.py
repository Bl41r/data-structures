"""Implementation of a link-list data type in Python."""


class Node(object):

    def __init__(self, data, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        return str(self.data) + u', ' + str(self.next_node)


class LinkedList(object):

    def __init__(self, node_list):
        """Initialize the linked list instance."""

        self.head = None
        self.tail = Node(node_list[0])
        self.length = 0
        for node in node_list:
            self.length += 1
            self.head = Node(node, self.head)

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
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        popped_node = self.head
        self.head = self.head.next_node
        self.length -= 1
        return popped_node.data

    def search(self, val):
        """Return the node containing val in the list, if exists, else None."""
        pass

    def size(self):
        """Return the length of the list."""
        return self.length

    def remove(node):
        """Remove the given node from the list, wherever it might be."""
        pass
