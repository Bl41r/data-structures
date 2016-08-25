# -*- coding: utf-8 -*-
"""Simple graph implementation.

Simple graph data type which contains a list of nodes.
"""

from __future__ import unicode_literals


class Node(object):
    """Node class which has data, a unique name(string), and a list of neighboring node names."""

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
                if type(n) == str:
                    self.neighbors.append(n)
                raise TypeError('Neighbors must be a list of node names.')

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
            output.append("{} to {}".format(self.name, n))
        return output


class SimpleGraph(object):
    """SimpleGraph class which has a dict of nodes.

    The name of each node is the key, with the Node ocject being the
    value contained.
    """

    def __init__(self):
        """Initialize the graph."""
        self.node_dict = {}

    def __repr__(self):
        """Display the list of nodes."""
        return repr(self.node_list)

    def add_node(self, n):
        """Add a node instance to the graph.

        Node must have a unique name.
        """
        pass

    def add_edge(self, n1, n2):
        """Add n2 to n1.neighbors.  If either don't exist, add to graph.

        n1 and n2 are Node instances.
        """
        pass

    def del_node(self, n):
        """Delete node from graph.

        Also removes the node from the neighbors list from other nodes
        contained in the the node_dict.
        """
        pass

    def has_node(self, n):
        """True if Node ‘n’ inst is contained in the graph.  Else false."""
        pass

    def neighbors(self, n):
        """Return the list of all nodes connected to ‘n’ by edges.

        Raises an error if n is not in g.
        """
        pass

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting n1 and n2.

        False if not, raises an error if either of the supplied nodes
        are not in g.
        """
        pass
