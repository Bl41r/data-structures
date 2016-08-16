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

        self.head = None
        self.tail = Node(node_list[0])

        for node in self.node_list:
            self.head = Node(node, self.head)

        self.length = len(node_list)    # make sure to inc/dec with push/remove

    def __repr__(self):
        """Display the linked list."""
        return str(self.head)

    def __len__(self):
        return self.length
