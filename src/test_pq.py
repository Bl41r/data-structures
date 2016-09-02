# -*- coding: utf-8 -*-

"""This is the test file for the priority queue module. Expected behavior below:"""

from __future__ import unicode_literals
from collections import namedtuple
import pytest
import random
import string
import itertools

'''

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
             random.randrange(5, 100)) for n in range(10)
             ]


STR_CASES = [random.sample(string.printable,
             random.randrange(2, 100)) for n in range(10)
             ]

TEST_CASES = EDGE_CASES + INT_CASES + STR_CASES

MyPQFix = namedtuple(
    'pqFixture',
    ('pqueue', 'input_val', 'len_int_list', 'type_err')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def pq(request):
    '''return an empty Priority Queue'''
    from priorityq import PriorityQueue
    pqueue = PriorityQueue()
    input_val = None
    int_list_priority = []
    if type(request.param) is int:
        for val in request.param:
            int_list_priority.append(val)
    type_err = None
    if type(request.param) is not str():
        type_err = TypeError
    for val in request.param:
        try:
            input_val = val
        except:
            pass
    len_int_list = len(int_list_priority)
    int_list_priority = sorted(int_list_priority)
    return MyPQFix(pqueue, input_val, len_int_list, type_err)


def test_node_init(pq):
    from priorityq import PNode
    try:
        a = PNode(pq.input_val, pq.input_val)
        assert a.value == pq.input_val
    except ValueError:
        with pytest.raises(ValueError):
            PNode(pq.input_val, pq.input_val)


def test_insert_nonnode(pq):
    with pytest.raises(TypeError):
        pq.pqueue.insert(pq.input_val)


def test_insert_node(pq):
    from priorityq import PNode
    if pq.input_val is int():
        a = PNode(pq.input_val)
        b = PNode(pq.input_val * 2)
        c = PNode(pq.input_val * 3)
        d = PNode(pq.input_val * 4)
        e = PNode(pq.input_val * 5)
    pq.pqueue.insert(e)
    pq.pqueue.insert(c)
    pq.pqueue.insert(a)
    pq.pqueue.insert(d)
    pq.pqueue.insert(b)
    assert pq.pqueue.heap[0] == a
