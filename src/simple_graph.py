# -*- coding: utf-8 -*-
"""Simple graph implementation.

Simple graph data type which contains a list of nodes.  Nodes are a
class, which makes them adaptable for additional attributes to be added
onto.
"""

from __future__ import unicode_literals


class Node(object):
    """Node class.

    Has data, a unique name(string), and a list of neighboring
    node names.
    """

    def __init__(self, name, data=None):
        """Initialize the Node instance."""
        if type(name) != str:
            raise TypeError('Name must be a string.')
        self.name = name
        self.data = data
        self.neighbors = []

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
        return repr(self.node_dict)

    def add_node(self, n):
        """Add a node instance to the graph.

        Node must have a unique name.
        """
        if type(n) is not Node:
            raise TypeError('Arguments passed must be a Node instance.')
        if n.name in self.node_dict:
            raise KeyError('Node {} already exists as {}'.format(n.name, self))
        self.node_dict[n.name] = n

    def add_edge(self, n1, n2):
        """Add n2.name to n1.neighbors.

        If either don't exist, add to graph.  n1 and n2 are Node
        instances which should be contained in the graph's node_dict.
        If n1 already contains n2 as a neighbor, n2 will not be appended
        again.
        """
        try:
            if n1.name not in self.node_dict:
                self.add_node(n1)
            if n2.name not in self.node_dict:
                self.add_node(n2)
        except AttributeError:
            raise TypeError('Arguments must be Node instances.')

        if n1 is not self.node_dict[n1.name] or n2 is not self.node_dict[n2.name]:
            raise ValueError('Cannot Overwrite existing nodes in graph.')

        n1.neighbors.append(n2.name)
        n1.neighbors = list(set(n1.neighbors))

    def del_node(self, n):
        """Delete node from graph.

        Also removes the node from the neighbors list from other nodes
        contained in the the node_dict.
        """
        try:
            del self.node_dict[n.name]
        except KeyError:
            raise KeyError('Node does not exist in graph.')

        for key in self.node_dict:
            if n.name in self.node_dict[key].neighbors:
                del n.name

    def has_node(self, n):
        """True if Node ‘n’ inst is contained in the graph.  Else false."""
        try:
            node_in_graph = n.name in self.node_dict
        except AttributeError:
            raise TypeError('Must pass a node to has_node method.')
        return node_in_graph

    def neighbors(self, n):
        """Return the list of all nodes connected to ‘n’ by edges.

        Raises an error if n is not in g.
        """
        pass

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting n1 -> n2.

        False if not, raises an error if either of the supplied nodes
        are not in g.
        """
        pass
