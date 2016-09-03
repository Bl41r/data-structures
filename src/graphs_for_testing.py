"""Builds test graphs."""

from simple_graph import SimpleGraph
from simple_graph import Node


def build_search_graph1():
    r"""Construct and return a test graph.

       /-B--D \
      A    /   F
       \-C --E/
    """

    a = Node('a_node', 0)
    b = Node('b_node', 8)
    c = Node('c_node', 5)
    d = Node('d_node', 7)
    e = Node('e_node', 12)
    f = Node('f_node', 3)

    gr = SimpleGraph()
    gr.add_node(a)
    gr.add_node(b)
    gr.add_node(c)
    gr.add_node(d)
    gr.add_node(e)
    gr.add_node(f)
    gr.add_edge(a, b)
    gr.add_edge(a, c)
    gr.add_edge(b, d)
    gr.add_edge(c, d)
    gr.add_edge(c, e)
    gr.add_edge(e, f)
    gr.add_edge(d, f)

    return gr


def build_search_graph2():
    """Construct and return a test graph.

    Like graph1, but different weights.
    """

    a = Node('a_node', 0)
    b = Node('b_node', 1)
    c = Node('c_node', 5)
    d = Node('d_node', 1)
    e = Node('e_node', 12)
    f = Node('f_node', 3)

    gr = SimpleGraph()
    gr.add_node(a)
    gr.add_node(b)
    gr.add_node(c)
    gr.add_node(d)
    gr.add_node(e)
    gr.add_node(f)
    gr.add_edge(a, b)
    gr.add_edge(a, c)
    gr.add_edge(b, d)
    gr.add_edge(b, e)
    gr.add_edge(c, d)
    gr.add_edge(c, e)
    gr.add_edge(e, f)
    gr.add_edge(d, f)

    return gr


def build_search_graph3():
    r"""Construct and return a test graph.

       /-B--D
      A   `/,    F
       \-C --E
    Nothing connects to F, and B and E now connected.
    """

    a = Node('a_node', 0)
    b = Node('b_node', 1)
    c = Node('c_node', 5)
    d = Node('d_node', 1)
    e = Node('e_node', 12)
    f = Node('f_node', 3)

    gr = SimpleGraph()
    gr.add_node(a)
    gr.add_node(b)
    gr.add_node(c)
    gr.add_node(d)
    gr.add_node(e)
    gr.add_node(f)
    gr.add_edge(a, b)
    gr.add_edge(a, c)
    gr.add_edge(b, d)
    gr.add_edge(b, e)
    gr.add_edge(c, d)
    gr.add_edge(c, e)

    return gr
