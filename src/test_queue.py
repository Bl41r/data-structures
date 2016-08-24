# -*- coding: utf8 -*-
from __future__ import unicode_literals
from collections import namedtuple
import pytest

''' This is the test file for the Queue module.'''

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

MyQueueFix = namedtuple(
    'QueueFixture',
    ('instance', 'first', 'seq', 'pop_error', 'size', 'last')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def queue(request):
    '''Return an empty queue'''
    from dbl_lnk_lst import Queue
    instance = Queue()
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
    return MyQueueFix(instance, first, seq, pop_error, size, last)


def test_init(queue):
    pass


def test_size(queue):
    assert queue.instance.size() == queue.size


def test_display(queue):
    assert queue.instance.display() == str(queue.instance)


def test_pop(queue):
    if queue.pop_error is None:
        assert queue.instance.pop() == queue.last
    else:
        with pytest.raises(queue.pop_error):
            queue.instance.pop()


def test_shift(queue):
    if queue.pop_error is None:
        assert queue.instance.shift() == queue.first
        assert queue.instance.size() == queue.size - 1
    else:
        with pytest.raises(queue.pop_error):
            queue.instance.shift()


def test_push(queue):
    assert queue.instance.push(8).head.data == 8
    assert queue.instance.size() == queue.size + 1
