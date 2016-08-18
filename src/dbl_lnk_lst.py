"""Implementation of a link-list data type in Python."""


class Node_Dll(object):

    def __init__(self, data, prev_node=None, next_node=None):
        """Initialize the Node instance."""
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        """Display the data in this node."""
        if self.next_node is not None:
            return str(self.data) + u', ' + str(self.next_node)
        else:
            return str(self.data)


class Dll(object):

    def __init__(self, params=None):
        """Initialize the linked list instance."""

        self.length = 0

        if hasattr(params, '__iter__'):
            for node in params:
                self.push(node)
        elif params:
            self.push(params)

    def __repr__(self):
        """Display the linked list."""
        try:
            return u'(' + str(self.head) + u')'
        except AttributeError:
            return u'()'

    def __len__(self):
        return self.length

    def display(self):
        """
        Return a unicode string representing
        the list as if it were a Python tuple.
        """
        self.__repr__()

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

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        if self.length > 0:
            popped_node = self.head
            self.head.next_node.prev_node = None
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
        if self.length > 0:
            shifted_node = self.tail
            self.tail = self.tail.prev_node
            self.tail.next_node = None
            self.length -= 1
            return shifted_node.data
        else:
            return None
