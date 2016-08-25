# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from collections import namedtuple
import pytest
import random

''' This is the test file for the linked_list module. Expected behavior below.

    insert(value, next=None): Inserts the specified value as a new Node at
    the end of the Linked List.

    remove(value): Searches the Linked List for the value specified.
    If a Node with that value is found, returns that Node.

    search(value): Searches Linked List for a Node with the value specified,
    if there is no Node with that value, returns None.

    display(): Displays all Nodes in the Linked List.

    pop(): Removes a Node and returns the value.
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

MyLLFix = namedtuple(
    'LLFixture',
    ('instance', 'first', 'seq', 'pop_error', 'size', 'last', 'remove_val', 'sequence_after_remove', 'remove_error')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def ll(request):
    '''return an empty LinkedList'''
    from linked_list import LinkedList
    instance = LinkedList()
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
        remove_error = TypeError
        last = None
        remove_val = None
        sequence_after_remove = None
    for val in request.param:
        instance.push(val)
    return MyLLFix(instance, first, seq, pop_error, size, last, remove_val, sequence_after_remove, remove_error)


def test_push(ll):
    '''Test the push function'''
    ll.instance.push(ll.size)
    assert ll.instance.head.data == ll.size


def test_display(ll):
    '''Test the display function'''
    assert ll.instance.display() == str(ll.instance)


def test_pop(ll):
    '''Test the pop function'''
    assert ll.instance.pop() == ll.last


def test_search(ll):
    '''Test the search function'''
    if ll.instance.head is not None:
        assert ll.instance.search(ll.first).data == ll.first


def test_size(ll):
    '''Test the size function'''
    assert ll.instance.size() == ll.size


def test_remove_valid(ll):
    '''Test the remove function'''
    if ll.remove_val is None:
        pytest.skip()
    ll.instance.remove(ll.instance.search(ll.remove_val))
    result = list(reversed(ll.sequence_after_remove))
    output = [ll.instance.pop() for n in ll.sequence_after_remove]
    assert result == output


def test_single_int():
    '''Test linkedlist __init__ with a single integer'''
    from linked_list import LinkedList
    with pytest.raises(TypeError):
        assert LinkedList(1)

def test_single_none():
    '''Test the linkedlist remove function with an empty remove value'''
    from linked_list import LinkedList
    l = LinkedList([])
    s = l.search([])
    with pytest.raises(AttributeError):
        assert l.remove([])
