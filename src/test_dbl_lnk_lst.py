# -*- coding: utf8 -*-
from __future__ import unicode_literals
from collections import namedtuple
import pytest
import random

''' This is the test file for the dll module.'''

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
    ('instance', 'first', 'seq', 'pop_error', 'size', 'last', 'remove_val', 'sequence_after_remove', 'remove_error')
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
        remove_error = None
        last = seq[-1]
        random_idx = random.randrange(len(seq))
        remove_val = seq[random_idx]
        sequence_after_remove = seq[:random_idx] + seq[random_idx + 1:]
    else:
        first = None
        pop_error = IndexError
        remove_error = ValueError
        last = None
        remove_val = None
        sequence_after_remove = None
    for val in request.param:
        instance.push(val)
    return MyDllFix(instance, first, seq, pop_error, size, last, remove_val, sequence_after_remove, remove_error)


def test_init(dll):
    pass


def test_size(dll):
    assert dll.instance.size() == dll.size


def test_display(dll):
    assert dll.instance.display() == str(dll.instance)


def test_pop(dll):
    if dll.pop_error is None:
        assert dll.instance.pop() == dll.last
    else:
        with pytest.raises(dll.pop_error):
            dll.instance.pop()


def test_shift(dll):
    if dll.pop_error is None:
        assert dll.instance.shift() == dll.first
        assert dll.instance.size() == dll.size - 1
    else:
        with pytest.raises(dll.pop_error):
            dll.instance.shift()


def test_push(dll):
    assert dll.instance.push(8).head.data == 8
    assert dll.instance.size() == dll.size + 1


def test_append(dll):
    assert dll.instance.append(8).tail.data == 8
    assert dll.instance.size() == dll.size + 1


def test_search(dll):
    if hasattr(dll.instance.head, 'data'):
        assert dll.instance.search(dll.first).data == dll.first
    assert dll.instance.search('asdfasdf') is None


def test_remove_valid(dll):
    if dll.remove_val is None:
        pytest.skip()
    dll.instance.remove(dll.remove_val)
    result = list(reversed(dll.sequence_after_remove))
    output = [dll.instance.pop() for n in dll.sequence_after_remove]
    assert result == output


def test_remove_value_error(dll):
    if dll.remove_error is not None:
        with pytest.raises(dll.remove_error):
            dll.instance.remove(dll.remove_val)
