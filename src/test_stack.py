# -*- coding: utf-8 -*-
"""This is the test file for the stack module. Expected behavior below."""
from __future__ import unicode_literals
from collections import namedtuple
import pytest


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

MyStackFix = namedtuple(
    'StackFixture',
    ('instance', 'first', 'seq', 'pop_error', 'size', 'last')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def stack(request):
    """Return an empty stack for tests."""
    from stack import Stack
    instance = Stack()
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
    return MyStackFix(instance, first, seq, pop_error, size, last)


def test_push(stack):
    """Test the push function."""
    stack.instance.push(stack.size)
    assert stack.instance._stack.head.data == stack.size


def test_pop(stack):
    """Test the pop function."""
    if stack.pop_error is None:
        assert stack.instance.pop() == stack.last
    else:
        with pytest.raises(stack.pop_error):
            stack.instance.pop()


def test_single_int():
    """Test stack __init__ with a single integer."""
    from stack import Stack
    with pytest.raises(TypeError):
        assert Stack(1)
