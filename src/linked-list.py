"""Implementation of a link-list data type in Python."""


class Node(object):

    def __init__(self, data, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        return str(self.data) + ', ' + str(self.next_node)


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
        return '(' + str(self.head) + ')'

    def __len__(self):
        return self.length

    def display(self):
        pass

    def push(self, val):
        pass

    def pop(self):
        pass

    def search(self, val):
        pass

    def size(self):
        return self.length

    def remove(node):
        pass
