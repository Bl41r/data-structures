"""Simple graph implementation.

Simple graph data type which contains a list of nodes.a
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
        self.neighbors = []

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
        output = []
        for n in self.neighbors:
            output.append("{} to {}".format(self.name, n.name))
        return output


class SimpleGraph(object):
    """SimpleGraph class which has a list of nodes, several methods.."""
