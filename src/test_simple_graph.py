# -*- coding: utf-8 -*-

"""This is the test file for the graph module. Expected behavior below:"""

from collections import namedtuple
import pytest
import random
import string


'''
g.nodes(): return a list of all nodes in the graph

g.edges(): return a list of all edges in the graph

g.add_node(n): adds a new node ‘n’ to the graph

g.add_edge(n1, n2, weight): adds a new edge to the graph connecting ‘n1’ and ‘n2’,
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
    ('graph', 'input_val', 'weight', 'length', 'type_err')
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
    weight = 5
    return MySGFix(graph, input_val, weight, length, type_err)


# Testing basic Node object creation

def test_node_init(sg):
    """
    Create node from random inputs ensuring only string inputs create nodes
    """
    from simple_graph import Node
    try:
        a = Node(sg.input_val, sg.weight)
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
    a = Node(strung_input)
    if a.data:
        assert repr(a) == repr(strung_input)

# Test all add node to graph functions


def test_sg_add_node(sg):
    """
    Test addition of single node to simple_graph. Non-node type objects should
    raise a type error.
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    sg.graph.add_node(a)
    assert a.name in sg.graph.node_dict


def test_sg_add_node_quick(sg):
    """
    Test addition of single node to simple_graph. Non-node type objects should
    raise a type error.
    """
    from simple_graph import Node
    strung_input = str(sg.input_val)
    sg.graph.add_node_quick(strung_input)
    assert strung_input in sg.graph.node_dict


def test_sg_add_existing_node(sg):
    """
    Test addition of an existing node to simple_graph. Expected KeyError.
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
    sg.graph.add_edge(a, b, sg.weight)
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
    sg.graph.add_edge(a, b, sg.weight)
    assert a.neighbors[0][0] == b.name


def test_sg_add_edge_by_name(sg):
    """
    Test addition of an edge to simple_graph. Node b is expected to be in node
    a's neighbors list
    """
    strung_input = str(sg.input_val)
    a = strung_input
    b = strung_input + 'a'
    sg.graph.add_node_quick(a)
    sg.graph.add_node_quick(b)
    sg.graph.add_edge_by_name(a, b, sg.weight)
    assert sg.graph.node_dict[a].neighbors[0][0] == b


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
        sg.graph.add_edge(a, b, sg.weight)


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


def test_del_node_by_name(sg):
    """
    Test deletion of node from simple_graph.
    """
    strung_input = str(sg.input_val)
    sg.graph.add_node_quick(strung_input)
    sg.graph.add_node_quick(strung_input + 'a')
    sg.graph.add_edge_by_name(strung_input, strung_input + 'a', 2)
    sg.graph.del_node_by_name(strung_input)
    assert strung_input not in sg.graph.node_dict
    assert strung_input not in sg.graph.node_dict[strung_input + 'a'].neighbors


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
    from simple_graph import SimpleGraph
    from simple_graph import Node
    strung_input = str(sg.input_val)
    print(strung_input)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    print(b.name)
    print(a.name)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.add_edge(a, b, sg.weight)
    sg.graph.del_node(b)
    assert b.name not in sg.graph.node_dict


def test_sg_edges(sg):
    """
    Test display of all edges in simple_graph. Node b is expected to be in node
    a's neighbors list.
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
    sg.graph.add_edge(a, c, 1)
    sg.graph.add_edge(b, d, 1)
    sg.graph.add_edge(a, d, 1)
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
    sg.graph.add_edge(a, b, sg.weight)
    c = sg.graph.neighbors(a)
    assert b.name in c[0][0]


def test_neighbors_by_name(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.add_edge(a, b, sg.weight)
    c = sg.graph.neighbors_by_name(strung_input)
    assert b.name in c[0][0]


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
    sg.graph.add_edge(a, b, sg.weight)
    assert sg.graph.adjacent(a, b)

def test_adjacent_by_name(sg):
    from simple_graph import Node
    strung_input = str(sg.input_val)
    a = Node(strung_input)
    b = Node(strung_input * 2)
    sg.graph.add_node(a)
    sg.graph.add_node(b)
    sg.graph.add_edge(a, b, sg.weight)
    assert sg.graph.adjacent_by_name(a.name, b.name)


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


def test_one_node_trav():
    """Assert both breadth and depth traversal return correct list.

    This graph has one node that is connected to itself.
    """
    from simple_graph import SimpleGraph
    from simple_graph import Node

    a = Node('a_node')
    gr = SimpleGraph()
    gr.add_node(a)
    gr.add_edge(a, a, 1)
    depth = gr.breadth_first_traversal(gr.node_dict['a_node'])
    breadth = gr.depth_first_traversal(gr.node_dict['a_node'])
    assert len(depth) == len(breadth) == 1


def test_breadth_ft():
    """Test breadth traverse on more complicated graphs.

    One graph contains an edge from d to a, making it circular.
    """
    gr_tree = build_test_graph()
    gr_circ = build_test_graph('circular')

    tree = gr_tree.breadth_first_traversal(gr_tree.node_dict['a_node'])
    circ = gr_circ.breadth_first_traversal(gr_circ.node_dict['a_node'])

    a = tree.index('a_node')
    b = tree.index('b_node')
    c = tree.index('c_node')
    d = tree.index('d_node')
    e = tree.index('e_node')
    f = tree.index('f_node')
    g = tree.index('g_node')
    h = tree.index('h_node')
    i = tree.index('i_node')

    assert a == 0
    assert b == 1 or b == 2
    assert c == 1 or c == 2
    assert d == 3 or d == 4 or d == 5 or d == 6
    assert g == 3 or g == 4 or g == 5 or g == 6
    assert f == 3 or f == 4 or f == 5 or f == 6
    assert e == 3 or e == 4 or e == 5 or e == 6
    assert h == 7 or h == 8
    assert i == 7 or i == 8

    assert len(tree) == len(circ)


def test_depth_ft():
    """Test depth traverse on more complicated graphs.

    One graph contains an edge from d to a, making it circular.
    """
    gr_tree = build_test_graph()
    gr_circ = build_test_graph('circular')

    tree = gr_tree.depth_first_traversal(gr_tree.node_dict['a_node'])
    circ = gr_circ.depth_first_traversal(gr_circ.node_dict['a_node'])

    a = tree.index('a_node')
    b = tree.index('b_node')
    c = tree.index('c_node')
    d = tree.index('d_node')
    e = tree.index('e_node')
    f = tree.index('f_node')
    g = tree.index('g_node')
    h = tree.index('h_node')
    i = tree.index('i_node')

    assert a == 0
    assert b == 1 or 2
    assert c == 1 or c == 6
    assert d == b + 1 or d == b + 4
    assert e == b + 1 or b + 2
    assert f == c + 1 or c + 2
    assert g == c + 1 or f + 1
    assert h == e + 1 or h == e + 2
    assert i == e + 1 or h + 1

    assert len(tree) == len(circ)


def test_weight_by_name():
    """Test weight functionality."""
    from simple_graph import SimpleGraph
    gr = SimpleGraph()
    gr.add_node_quick('a')
    gr.add_node_quick('b')
    gr.add_edge_by_name('a', 'b', 5)
    assert gr.weight_by_name('a', 'b') == 5


def test_weight():
    """Test weight functionality."""
    from simple_graph import Node
    from simple_graph import SimpleGraph
    gr = SimpleGraph()
    a = Node('a')
    b = Node('b')
    gr.add_node(a)
    gr.add_node(b)
    gr.add_edge_by_name('a', 'b', 5)
    assert gr.weight(a, b) == 5
