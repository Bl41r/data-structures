# -*- coding: utf-8 -*-
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
    [1, 3, 5]
]

MyDequeFix = namedtuple(
    'DequeFixture',
    ('instance', 'first', 'seq', 'pop_error', 'size', 'last')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def deque(request):
    '''return an empty deque'''
    from deque import Deque
    instance = Deque()
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
        instance.appendleft(val)
    return MyDequeFix(instance, first, seq, pop_error, size, last)


def test_deque_pop(deque):
    assert deque.instance.pop() == deque.first


def test_deque_popleft(deque):
    assert deque.instance.popleft() == deque.last


def test_append(deque):
    if deque.first is not None:
        assert deque.instance.append(0)._deque.tail.data == 0


def test_appendleft(deque):
    if deque.first is not None:
        assert deque.instance.appendleft(1)._deque.head.data == 1


def test_peek(deque):
    if deque.first is not None:
        assert deque.instance.peek() == deque.first


def test_peekleft(deque):
    if deque.first is not None:
        assert deque.instance.peekleft() == deque.last


def test_size(deque):
    assert deque.instance.size() == deque.size
