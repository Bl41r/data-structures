# -*- coding: utf-8 -*-

"""This is the test file for the binheap module. Expected behavior below:"""

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

MyBHFix = namedtuple(
    'BHFixture',
    ('heap', 'input_val', 'length', 'type_err')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def bin(request):
    '''return an empty Simple Graph'''
    from bin import bin

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
    return MyBINFix(graph, input_val, length, type_err)


def test_node_init(bin):
    from simple_graph import Node
    try:
        a = Node(bin.input_val)
        assert a.name == pq.input_val
    except TypeError:
        with pytest.raises(TypeError):
            Node(bin.input_val)
