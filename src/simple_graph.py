"""Implementation of a simple graph data type in Python containing 

nodes.
"""

from __future__ import unicode_literals


class Node(object):
    """Node class which has data, a unique name(string), and a list of neighboring nodes."""
    def __init__(self, name, data=None, neighbors=[]):
        """Initialize the Node instance."""
        if type(name) != str:
            raise TypeError('Name must be a string.')
        self.name = name
        self.data = data

        try:
            self.neighbors = list(set(neighbors))
            for n in neighbors:
                if type(n) == Node:
                    self.neighbors.append(n)
                raise TypeError('Neighbors must be a list of nodes.')

        except TypeError:
            if neighbors is not None:
                raise TypeError('This function requires an iterable value.')

    def __repr__(self):
        """Display the data in this node."""
        return repr(self.data)

    def output_neighbors(self):
        """Return a list of strings indicating its neighbors."""


class SimpleGraph(object):
    """SimpleGraph class which has a list of nodes, several methods.."""