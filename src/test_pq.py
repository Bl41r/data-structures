# -*- coding: utf-8 -*-

"""This is the test file for the priority queue module. Expected behavior below:"""

from __future__ import unicode_literals
from collections import namedtuple
import pytest
import random
import string


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
             random.randrange(2, 100)) for n in range(10)
             ]


STR_CASES = [random.sample(string.printable,
             random.randrange(2, 100)) for n in range(10)
             ]

TEST_CASES = EDGE_CASES + INT_CASES + STR_CASES

MyPQFix = namedtuple(
    'pqFixture',
    ('pqueue', 'input_val', 'length', 'type_err')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def pq(request):
    '''return an empty Priority Queue'''
    from priorityq import priorityq

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
    return MyPQFix(pqueue, input_val, length, type_err)


def test_node_init(pq):
    from priorityq import PNode
    try:
        a = Node(pq.input_val)
        assert a.name == pq.input_val
    except TypeError:
        with pytest.raises(ValueError):
            Node(pq.input_val)
