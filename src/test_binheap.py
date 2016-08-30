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
    ('binheap', 'input_val', 'int_list', 'str_list')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def bin(request):
    '''return an empty BinHeap'''
    from binheap import MinHeap
    binheap = MinHeap()
    int_list = []
    str_list = []
    for val in request.param:
        try:
            input_val = val
            if val is type(int):
                int_list.append(val)
            elif val is type(str):
                str_list.append(val)
        except:
            pass
    return MyBHFix(binheap, input_val, int_list, str_list)


def test_node_init(bin):
    a = bin.binheap(bin.int_list)
    assert len(a) == len(bin.int_list)
