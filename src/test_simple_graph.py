# -*- coding: utf-8 -*-

"""This is the test file for the graph module. Expected behavior below:"""

from __future__ import unicode_literals
from collections import namedtuple
import pytest
import random
import string


'''
g.nodes(): return a list of all nodes in the graph

g.edges(): return a list of all edges in the graph

g.add_node(n): adds a new node ‘n’ to the graph

g.add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’,
if either n1 or n2 are not already present in the graph, they should be added.

g.del_node(n): deletes the node ‘n’ from the graph,
raises an error if no such node exists

g.del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph,
raises an error if no such edge exists

g.has_node(n): True if node ‘n’ is contained in the graph, False if not.

g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises
an error if n is not in g

g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2,
False if not, raises an error if either of the supplied nodes are not in g
'''


EDGE_CASES = [
    {},
    [],
    {'a': 0},
    [1, 2, 3],
    'Æ',
    ''
]

INT_CASES = [random.sample(range(1000),
             random.randrange(2, 100)) for n in range(10)
             ]


STR_CASES = [random.sample(string.printable,
             random.randrange(2, 100)) for n in range(10)
             ]

TEST_CASES = EDGE_CASES + INT_CASES + STR_CASES

MySGFix = namedtuple(
    'SGFixture',
    ('graph', 'input_val', 'length', 'type_err')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def sg(request):
    '''return an empty Simple Graph'''
    from simple_graph import SimpleGraph
    graph = SimpleGraph()
    if type(request.param) is not int():
        length = len(request.param)
    type_err = None
    input_val = None
    if type(request.param) is not str():
        type_err = TypeError
    for val in request.param:
        input_val = val
    return MySGFix(graph, input_val, length, type_err)


# Testing basic Node object creation

def test_node_init(sg):
    """
    Create node from random inputs ensuring only string inputs create nodes
    """
    from simple_graph import Node
    try:
        a = Node(sg.input_val)
        assert a.name == sg.input_val
    except TypeError:
        with pytest.raises(TypeError):
            Node(sg.input_val)


def test_node_repr(sg):
    """
    Test implementation of the repr builtin to return stringified node.data
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input, strung_input)
    if a.data:
        assert repr(a) == repr(strung_input)

# Test all add node to graph functions


def test_sg_add_new_node(sg):
    """
    Test addition of single node to simple_graph. Non-node type objects should
    raise a type error.
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    sg.graph.add_node(a)
    assert a.name in sg.graph.node_dict


def test_sg_add_existing_node(sg):
    """
    Test addition of an existing node to simple_graph. Expected KeyError
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input)
    sg.graph.add_node(a)
    with pytest.raises(KeyError):
        sg.graph.add_node(b)


def test_sg_add_nonnode(sg):
    """
    Test addition of a non-node-type to simple_graph. Expected ValueError
    """
    strung_input = str(sg.input_val)
    with pytest.raises(TypeError):
        sg.graph.add_node(strung_input)

# Test all add edge to graph functions


def test_sg_add_edge_create_node(sg):
    """
    Test addition of an edge to simple_graph. Nodes are expected to be created
    if they don't exist already
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_edge(a, b)
    assert a.name in sg.graph.node_dict and b.name in sg.graph.node_dict


def test_sg_add_edge(sg):
    """
    Test addition of an edge to simple_graph. Node b is expected to be in node
    a's neighbors list
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.add_edge(a, b)
    assert a.neighbors[0] == b.name


def test_sg_add_edge_nonnode(sg):
    """
    Test addition of an edge to simple_graph with a non-node-type.
    TypeError expected
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = strung_input
    sg.graph.add_node(a)
    with pytest.raises(TypeError):
        sg.graph.add_edge(a, b)


# Test delete node functions


def test_del_node(sg):
    """
    Test deletion of node from simple_graph.
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.del_node(a)
    assert a.name not in sg.graph.node_dict


def test_del_nonexist_node(sg):
    """
    Test deletion of node from simple_graph.
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    sg.graph.add_node(a)
    sg.graph.del_node(a)
    with pytest.raises(KeyError):
        sg.graph.del_node(a)


def test_del_node_and_edge(sg):
    """
    Test deletion of node from simple_graph.
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.add_edge(a, b)
    sg.graph.del_node(b)
    assert len(a.neighbors) == 0


def test_sg_edges(sg):
    """
    Test display of all edges in simple_graph. Node b is expected to be in node
    a's neighbors list
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    c = Node(strung_input * 3)
    d = Node(strung_input * 4)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.add_node(c)
    sg.graph.add_node(d)
    sg.graph.add_edge(a, c)
    sg.graph.add_edge(b, d)
    sg.graph.add_edge(a, d)
    e = a.output_neighbors()
    f = b.output_neighbors()
    g = e + f
    h = sg.graph.edges()
    assert len(g) == len(h)


def test_has_node(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    sg.graph.add_node(a)
    assert sg.graph.has_node(a)


def test_has_node_non_node(sg):
    with pytest.raises(TypeError):
        sg.graph.has_node(sg.input_val)


def test_neighbors(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.add_edge(a, b)
    c = sg.graph.neighbors(a)
    assert b.name in c


def test_neighbors_no_arg(sg):
    strung_input = str(sg.input_val)
    with pytest.raises(TypeError):
        sg.graph.neighbors(strung_input)


def test_neighbors_no_node(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    with pytest.raises(ValueError):
        sg.graph.neighbors(a)


def test_adjacent(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.add_edge(a, b)
    assert sg.graph.adjacent(a, b)


def test_adjacent_missing_node(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_node(a)
    with pytest.raises(ValueError):
        assert sg.graph.adjacent(a, b)


def test_adjacent_non_node(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    sg.graph.add_node(a)
    with pytest.raises(TypeError):
        assert sg.graph.adjacent(a, strung_input)


def test_sg_nodes_in_graph(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    c = Node(strung_input * 5)
    d = Node(strung_input * 3)
    e = Node(strung_input * 4)
    sg.graph.add_node(a)
    sg.graph.add_node(c)
    sg.graph.add_node(d)
    sg.graph.add_node(e)
    sg.graph.add_node(b)
    result = sg.graph.nodes()
    assert len(result) == 5
