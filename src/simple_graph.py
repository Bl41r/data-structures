# -*- coding: utf-8 -*-
"""Simple graph implementation.

Simple graph data type which contains a dict of nodes.  Nodes are a
class, which makes them adaptable for additional attributes to be added.
In this implementation, weight is an integer, and the weight of an edge
is calculated to be the abs value of the difference between the weights
of two nodes.
"""

import sys
import timeit


class Node(object):
    """Node class.

    Has data, a unique name(string), and a list of neighboring
    node names.
    """

    def __init__(self, name, weight=0, data=None):
        """Initialize the Node instance."""
        if not isinstance(name, type('')):
            raise TypeError('Name must be a string.')
        if not isinstance(weight, int):
            raise TypeError('Weight must be an integer.')
        self.name = name
        self.weight = abs(weight)
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
            name = n.name
            del self.node_dict[n.name]
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

    def neighbors(self, n):
        """Return the list of all nodes connected to ‘n’ by edges.

        Raises an error if n is not in g.
        """
        try:
            node_list = self.node_dict[n.name].neighbors
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
            n_adjacent = self.node_dict[n2.name].name in self.node_dict[n1.name].neighbors
        except KeyError:
            raise ValueError('Graph does not contain both nodes.  Use has_node method.')
        except AttributeError:
            raise TypeError('Must pass node types to adjacent method.')
        return n_adjacent

    def nodes(self):
        """Return a list of all node names contained in graph."""
        tmp = []
        for key in self.node_dict:
            tmp.append(key)
        return tmp

    def weight(self, n1, n2):
        """Return the relative weight of an edge.  n1 and n2 are nodes."""
        try:
            return abs(self.node_dict[n1.name].weight - self.node_dict[n2.name].weight)
        except AttributeError:
            raise AttributeError('n1 and n2 must be nodes.')
        except KeyError:
            raise KeyError('Nodes must be contained in the graph.')

    # Traversal methods
    def depth_first_traversal(self, start):
        """Perform a depth traversal.  'start' is a node."""
        curr = [start]
        ret = []

        while len(curr):
            c = curr.pop()
            ret.append(c.name)
            for n in c.neighbors:
                if self.node_dict[n].name not in ret:
                    curr.append(self.node_dict[n])
        return ret

    def breadth_first_traversal(self, start):
        """Perform a breadth traversal.  'start' is a node."""
        breadth_list = [start.name]
        for edge in breadth_list:
            tmp = self.neighbors(self.node_dict[edge])
            for e in tmp:
                if e not in breadth_list:
                    breadth_list.append(e)
        return breadth_list

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: "python3 simple_graph.py <demo-type>" <demo-type> can be either circular, tree, or struct.')
        sys.exit(1)

    # build graph with nodes
    a = Node('a_node')
    b = Node('b_node')
    c = Node('c_node')
    d = Node('d_node')
    e = Node('e_node')
    f = Node('f_node')
    g = Node('g_node')
    h = Node('h_node')
    i = Node('i_node')
    gr = SimpleGraph()
    gr.add_node(a)
    gr.add_node(b)
    gr.add_node(c)
    gr.add_node(d)
    gr.add_node(e)
    gr.add_node(f)
    gr.add_node(g)
    gr.add_node(h)
    gr.add_node(i)
    gr.add_edge(a, b)
    gr.add_edge(a, c)
    gr.add_edge(b, d)
    gr.add_edge(b, e)
    gr.add_edge(c, f)
    gr.add_edge(c, g)
    gr.add_edge(e, h)
    gr.add_edge(e, i)

    if sys.argv[1] == 'circular':
        gr.add_edge(d, a)
        print('depth:', gr.depth_first_traversal(a))
        print('breadth', gr.breadth_first_traversal(a))
        print('10,000 times')
        t = timeit.timeit(lambda: gr.depth_first_traversal(a), number=10000)
        print('time for depth:', t)
        t = timeit.timeit(lambda: gr.breadth_first_traversal(a), number=10000)
        print('time for breadth:', t)
        sys.exit(0)

    if sys.argv[1] == 'tree':
        print('depth:', gr.depth_first_traversal(a))
        print('breadth', gr.breadth_first_traversal(a))
        print('10,000 times')
        t = timeit.timeit(lambda: gr.depth_first_traversal(a), number=10000)
        print('time for depth:', t)
        t = timeit.timeit(lambda: gr.breadth_first_traversal(a), number=10000)
        print('time for breadth:', t)
        sys.exit(0)

    if sys.argv[1] == 'struct':
        print('-- graph nodes ' + ('-----' * 7))
        for n in gr.node_dict:
            print('node name:', n, 'neighbors:', gr.node_dict[n].neighbors)
        print('-----' * 10)
        print('With tree chosen, no nodes are connected circularly.')
        print('If circular chosen, d_node connects to a_node.')
        sys.exit(0)

    print('expecting "circular", "tree", or "struct".')
    sys.exit(1)
