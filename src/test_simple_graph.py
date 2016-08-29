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
    if type(request.param) is not str():
        type_err = TypeError
    for val in request.param:
        try:
            input_val = val
        except:
            pass
    return MySGFix(graph, input_val, length, type_err)


def test_node_init(sg):
    from simple_graph import Node
    try:
        a = Node(sg.input_val)
        assert a.name == sg.input_val
    except TypeError:
        with pytest.raises(TypeError):
            Node(sg.input_val)
