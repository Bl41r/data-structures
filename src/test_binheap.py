# -*- coding: utf-8 -*-

"""This is the test file for the binheap module. Expected behavior below:"""

from __future__ import unicode_literals
from collections import namedtuple
import pytest
import random
import string


# Test Cases

EDGE_CASES = [
    {},
    [],
    {'a': 0},
    [1, 2, 3],
    'Æ',
    ''
]

INT_CASES = [random.sample(range(1000),
             random.randrange(2, 16)) for n in range(10)
             ]


STR_CASES = [random.sample(string.printable,
             random.randrange(2, 16)) for n in range(10)
             ]

TEST_CASES = EDGE_CASES + INT_CASES + STR_CASES

# Binheap test fixture

MyBHFix = namedtuple(
    'BHFixture',
    ('binheap', 'input_val', 'int_list', 'str_list', 'len_int', 'len_str')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def bin(request):
    '''return an empty BinHeap'''
    from binheap import MinHeap
    binheap = MinHeap()
    int_list = []
    str_list = []
    input_val = None
    for val in request.param:
        input_val = val
        if type(val) is int:
            int_list.append(val)
        elif type(val) is str:
            str_list.append(val)
    len_int = len(int_list)
    len_str = len(str_list)
    int_list = sorted(int_list)
    str_list = sorted(str_list)
    return MyBHFix(binheap, input_val, int_list, str_list, len_int, len_str)

# MinHeap init tests


def test_bin_init(bin):
    """
    Tests the instantiation of the binheap. Checks to see if the length of the
    heap property is same as the length of the input list.
    """
    from binheap import MinHeap
    a = MinHeap(bin.int_list)
    assert len(a.heap) == bin.len_int


def test_bin_no_list(bin):
    """
    Tests MinHeap to ensure that a TypeError is thrown when any other type but
    a list is an input.
    """
    from binheap import MinHeap
    if type(bin.input_val) is not int and bin.input_val is not None:
        with pytest.raises(TypeError):
            MinHeap(bin.input_val)


def test_bin_no_int(bin):
    """
    Tests MinHeap to ensure that a TypeError is thrown when attempting to
    sort a heap not made of integers
    """
    from binheap import MinHeap
    if type(bin.input_val) is not None:
        with pytest.raises(TypeError):
            MinHeap(bin.input_val)


def test_bin_push_heap_length(bin):
    for i in bin.int_list:
        bin.binheap.push(i)
    assert len(bin.binheap.heap) == len(bin.int_list)


def test_bin_push_type_err(bin):
    for i in bin.str_list:
        with pytest.raises(TypeError):
            print(i)
            bin.binheap.push(i)


def test_bin_pop_order(bin):
    for i in bin.int_list:
        bin.binheap.push(i)
    result = [ bin.binheap.pop() for i in bin.int_list ]
    assert result == bin.int_list

def test_bin_pop_index_err(bin):
    with pytest.raises(IndexError):
        bin.binheap.pop()
