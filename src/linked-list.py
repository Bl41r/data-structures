"""Implementation of a link-list data type in Python."""


class Node(object):

    def __init__(self, data, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        return str(self.data) + ' --> ' + str(self.next_node)


class LinkedList(object):

    def __init__(self, node_list):
        """Initialize the linked list instance."""
        self.node_list = node_list
        self.length = len(node_list)

        self.head = None
        for node in self.node_list:
            self.head = Node(node, self.head)

    def __repr__(self):
        """Display the linked list."""
        return str(self.head)
