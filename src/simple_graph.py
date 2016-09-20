# -*- coding: utf-8 -*-
"""Simple graph implementation.

Simple edge-weighted graph data type which contains a dict of nodes.  Nodes are a
class, which makes them adaptable for additional attributes to be added.
In this implementation, weight is a positive integer directional edge.
"""
import sys
import timeit


class Node(object):
    """Node class.

    Has data, a unique name(string), and a list of neighboring
    node names.
    """

    def __init__(self, name, data=None):
        """Initialize the Node instance."""
        if not isinstance(name, type('')):
            raise TypeError('Name must be a string.')
        self.name = name
        self.data = data
        self.neighbors = []

    def __repr__(self):
        """Display the data in this node."""
        if hasattr(self, 'data'):
            return repr(self.data)
        return 'No data'

    def output_neighbors(self):
        """Return a list of strings indicating its neighbors."""
        output = []
        for n in self.neighbors:
            output.append("{} to {}, weight = {}".format(self.name, n[0], n[1]))
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

    def add_node_quick(self, name, data=None):
        """Add a node quickly to the graph by supplying a name to it."""
        if not isinstance(name, type('')):
            raise TypeError('Name must be a string.')
        self.add_node(Node(name, data))

    def add_edge(self, n1, n2, weight):
        """Add n2.name to n1.neighbors.

        If either don't exist, add to graph.  n1 and n2 are Node
        instances which should be contained in the graph's node_dict.
        If n1 already contains n2 as a neighbor, n2 will not be appended
        again.  Weight is a positive integer.
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

        try:
            weight = float(weight)
        except ValueError:
            raise ValueError('Weight must be a positive number.')
        if weight >= 0:
            n1.neighbors.append((n2.name, weight))
            n1.neighbors = list(set(n1.neighbors))
        else:
            raise ValueError('Weight must be >= 0')

    def add_edge_by_name(self, node_name1, node_name2, weight):
        """Add an edge by the name of the nodes."""
        if node_name1 in self.node_dict.keys() and node_name2 in self.node_dict.keys():
            try:
                weight = float(weight)
            except ValueError:
                raise ValueError('Weight must be a positive number.')
            if weight >= 0:
                self.node_dict[node_name1].neighbors.append((node_name2, weight))
                self.node_dict[node_name1].neighbors = list(set(self.node_dict[node_name1].neighbors))
            else:
                raise ValueError('Weight must be >= 0')

    def del_edge(self, n1, n2):
        """Delete an edge."""
        for tup in self.node_dict[n1.name].neighbors:
            if tup[0] == n2.name:
                n1.neighbors.remove(tup)

    def del_node(self, n):
        """Delete node from graph.

        Also removes the node from the neighbors list from other nodes
        contained in the the node_dict.
        """
        try:
            name = n.name
            del self.node_dict[n.name]
        except KeyError:
            raise KeyError('Node does not exist in graph.')

        for key in self.node_dict:
            if name in self.node_dict[key].neighbors:
                del name


    def del_node_by_name(self, name):
        """Delete a node using the name."""
        try:
            del self.node_dict[name]
        except KeyError:
            raise KeyError('Node does not exist in graph.')

        for key in self.node_dict:
            if name in self.node_dict[key].neighbors:
                del name

    def edges(self):
        """Return a list of all edges."""
        edges = []
        for node in self.node_dict:
            edges.extend(self.node_dict[node].output_neighbors())
        return edges

    def has_node(self, n):
        """True if Node ‘n’ inst is contained in the graph.  Else false."""
        try:
            node_in_graph = n.name in self.node_dict
        except AttributeError:
            raise TypeError('Must pass a node to has_node method.')
        return node_in_graph

    def has_node_by_name(self, name):
        """True if node called name is in the graph."""
        node_in_graph = name in self.node_dict
        return node_in_graph

    def neighbors(self, n):
        """Return the list of all nodes connected ‘n’ is connected to 

        by edges and weight of edge.  Raises an error if n is not in g.
        """
        try:
            node_list = self.node_dict[n.name].neighbors
        except AttributeError:
            raise TypeError('Must pass a node to neighbors method.')
        except KeyError:
            raise ValueError('Node is not contained within graph.')
        return node_list

    def neighbors_by_name(self, name):
        """Return neighbors connected to node called name."""
        try:
            node_list = self.node_dict[name].neighbors
        except AttributeError:
            raise TypeError('Must pass a node to neighbors method.')
        except KeyError:
            raise ValueError('Node is not contained within graph.')
        return node_list

    def adjacent(self, n1, n2):
        """Return True if there is an edge connecting n1 -> n2.

        False if not, raises an error if either of the supplied nodes
        are not in g.
        """
        try:
            for item in self.node_dict[n1.name].neighbors:
                if self.node_dict[n2.name].name in item:
                    return True
            return False
        except KeyError:
            raise ValueError('Graph does not contain both nodes.  Use has_node method.')
        except AttributeError:
            raise TypeError('Must pass node types to adjacent method.')

    def adjacent_by_name(self, name1, name2):
        """Same as adjacent with node names used."""
        try:
            for item in self.node_dict[name1].neighbors:
                if self.node_dict[name2].name in item:
                    return True
            return False
        except KeyError:
            raise ValueError('Graph does not contain both nodes.  Use has_node method.')

    def nodes(self):
        """Return a list of all node names contained in graph."""
        tmp = []
        for key in self.node_dict:
            tmp.append(key)
        return tmp
