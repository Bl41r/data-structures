# # -*- coding: utf-8 -*-
# """Test of dbl_lnk_lst.py."""
#
# import pytest
# from dbl_lnk_lst import Dll
#
# # format: (list of datas, length, head data, next node data, display, rem_val, search, shift)
# TEST_DATAS = [
#     ([5, 4, 3, 2, 1], 5, 1, 2, '(1, 2, 3, 4, 5)', 3, 1, 5),
#     (['z', 'y', 'x', 'w', 'v', 'u'], 6, 'u', 'v', "(u, v, w, x, y, z)", 'z', 'w', 'z'),
#     ([], 0, None, None, '(None)', 2, 1, None)
# ]

# -*- coding: utf8 -*-
from __future__ import unicode_literals
from collections import namedtuple
import pytest

''' This is the test file for the deque module. Expected behavior below.
    append(val): adds value to the end of the deque
    appendleft(val): adds a value to the front of the deque
    pop(): removes a value from the end of the deque
    and returns it (raises an exception if the deque is empty)
    popleft(): removes a value from the front of the deque
    and returns it (raises an exception if the deque is empty)
    peek(): returns the next value that would be returned by pop
    but leaves the value in the deque (returns None if the deque is empty)
    peekleft(): returns the next value that would be returned by popleft
    but leaves the value in the deque (returns None if the deque is empty)
    size(): returns the count of items in the queue (returns 0 if the queue is
    empty)
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
MyDllFix = namedtuple(
    'DequeFixture',
    ('instance', 'first', 'seq', 'pop_error', 'size', 'last')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def dll(request):
    '''return an empty deque'''
    from dbl_lnk_lst import Dll
    instance = Dll()
    seq = request.param
    size = len(seq)
    if seq:
        first = seq[0]
        pop_error = None
        last = seq[-1]
    else:
        first = None
        pop_error = IndexError
        last = None
    for val in request.param:
        instance.push(val)
    return MyDllFix(instance, first, seq, pop_error, size, last)


def test_init(dll):
    assert dll.instance.length == dll.size
    assert dll.instance.head.data == dll.last

def test_size(dll):
    assert dll.instance.size() == dll.size


def test_display(dll):
    assert dll.instance.display() == str(dll.instance)


def test_pop(dll):
    assert dll.instance.pop() == dll.last


def test_push(dll):
    assert dll.instance.push(8).head.data == 8
    assert dll.instance.size() == dll.size + 1


def test_shift(dll):
    if dll.instance.head.data is not None:
        assert dll.instance.shift() == dll.first
        assert dll.instance.size() == dll.size - 1


def test_search(dll):
    if dll.instance.head.data is not None:
        assert dll.instance.search(dll.first).data == dll.first


def test_remove(dll):
    if dll.instance.head.data is not None:
        assert dll.instance.remove(dll.first).tail.data == dll.seq[1]
