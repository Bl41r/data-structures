# -*- coding: utf-8 -*-

"""This is the test file for the graph module. Expected behavior below:"""

from __future__ import unicode_literals
from collections import namedtuple
import pytest
import random


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



TEST_CASES = [
    [],
    [1],
    [1, 2],
    [1, 3, 5],
    [-50, 0, 50],
    [-50, 25, -25, 0],
    ['a', 'b', 'c'],
    ['abc'],
    ['¡', '¢', '£'],
    ['¡¢£'],
    ['a¡', 2],
    ['', None, 0],
    [(), (), ()],
    [(1, 2), (3, 4), 4, 'string'],
    [{}, {}, {}],
    [{'key': 'value', 'key2': 'value2', 'key3': 'value3'},
     {'key4': 'value4', 'key5': 'value5', 'key6': 'value6'}],
    {},
    'string',
    'a',
]

MySGFix = namedtuple(
    'SGFixture',
    ('instance', 'first', 'seq', 'none_error', 'size', 'last', 'remove_val', 'sequence_after_remove', 'remove_error')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def sg(request):
    '''return an empty LinkedList'''
    from linked_list import LinkedList
    instance = SimpleGraph()
    seq = request.param
    size = len(seq)
    if seq:
        first = seq[0]
        pop_error = None
        remove_error = None
        last = seq[-1]
        random_idx = random.randrange(len(seq))
        remove_val = seq[random_idx]
        sequence_after_remove = seq[:random_idx] + seq[random_idx + 1:]
    else:
        first = None
        pop_error = IndexError
        remove_error = TypeError
        last = None
        remove_val = None
        sequence_after_remove = None
    for val in request.param:
        instance.push(val)
    return MySGFix(instance, first, seq, pop_error, size, last, remove_val, sequence_after_remove, remove_error)


def test_push()
    with pytest.raises(AttributeError):
        assert l.remove([])
