"""Builds test graphs."""

from simple_graph import SimpleGraph
from simple_graph import Node


def build_test_graph(type='tree'):
    """Construct and return a test graph.

    If type == 'circular, an edge from d to a is constructed as well.'
    """
    from simple_graph import SimpleGraph
    from simple_graph import Node

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
    gr.add_edge(a, b, 1)
    gr.add_edge(a, c, 2)
    gr.add_edge(b, d, 3)
    gr.add_edge(b, e, 4)
    gr.add_edge(c, f, 5)
    gr.add_edge(c, g, 6)
    gr.add_edge(e, h, 7)
    gr.add_edge(e, i, 8)

    if type == 'circular':
        gr.add_edge(d, a, 9)
    return gr


def build_search_graph1():
    r"""Construct and return a test graph.

       /-B--D \
      A    /   F
       \-C --E/
    """
    a = Node('a_node')
    b = Node('b_node')
    c = Node('c_node')
    d = Node('d_node')
    e = Node('e_node')
    f = Node('f_node')

    gr = SimpleGraph()
    gr.add_node(a)
    gr.add_node(b)
    gr.add_node(c)
    gr.add_node(d)
    gr.add_node(e)
    gr.add_node(f)
    gr.add_edge(a, b, 8)
    gr.add_edge(a, c, 5)
    gr.add_edge(b, d, 1)
    gr.add_edge(c, d, 2)
    gr.add_edge(c, e, 7)
    gr.add_edge(e, f, 9)
    gr.add_edge(d, f, 4)

    return gr


def build_search_graph2():
    """Construct and return a test graph.

    Like graph1, but different weights.
    """
    a = Node('a_node')
    b = Node('b_node')
    c = Node('c_node')
    d = Node('d_node')
    e = Node('e_node')
    f = Node('f_node')

    gr = SimpleGraph()
    gr.add_node(a)
    gr.add_node(b)
    gr.add_node(c)
    gr.add_node(d)
    gr.add_node(e)
    gr.add_node(f)
    gr.add_edge(a, b, 1)
    gr.add_edge(a, c, 5)
    gr.add_edge(b, d, 0)
    gr.add_edge(b, e, 11)
    gr.add_edge(c, d, 4)
    gr.add_edge(c, e, 7)
    gr.add_edge(e, f, 9)
    gr.add_edge(d, f, 2)

    return gr


def build_search_graph3():
    r"""Construct and return a test graph.

    This graph is mroe complex, and demonstrates the algorithm will
    go back and try another path when the cost higher than another 
    optional path to explore.
    """
    a = Node('a_node')
    b = Node('b_node')
    c = Node('c_node')
    d = Node('d_node')
    e = Node('e_node')
    f = Node('f_node')
    g = Node('g_node')
    gr = SimpleGraph()
    gr.add_node(a)
    gr.add_node(b)
    gr.add_node(c)
    gr.add_node(d)
    gr.add_node(e)
    gr.add_node(f)
    gr.add_node(g)
    gr.add_edge(a, b, 1)
    gr.add_edge(a, f, 2)
    gr.add_edge(b, c, 3)
    gr.add_edge(c, d, 4)
    gr.add_edge(d, e, 5)
    gr.add_edge(d, g, 6)
    gr.add_edge(b, g, 20)
    gr.add_edge(f, g, 5)
    return gr
