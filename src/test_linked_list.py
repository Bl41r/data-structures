# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from collections import namedtuple
import pytest

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
    ('instance', 'first', 'seq', 'pop_error', 'size', 'last')
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
        last = seq[-1]
    else:
        first = None
        pop_error = IndexError
        last = None
    for val in request.param:
        instance.push(val)
    return MyLLFix(instance, first, seq, pop_error, size, last)


def test_init(ll):
    assert ll.instance.length == ll.size
    assert ll.instance.head.data == ll.last


def test_size(ll):
    assert ll.instance.size() == ll.size


def test_display(ll):
    assert ll.instance.display() == str(ll.instance)


def test_pop(ll):
    assert ll.instance.pop() == ll.last


def test_push(ll):
    assert ll.instance.push(8).head.data == 8
    assert ll.instance.size() == ll.size + 1


def test_shift(ll):
    if ll.instance.head.data is not None:
        assert ll.instance.shift() == ll.first
        assert ll.instance.size() == ll.size - 1


def test_search(ll):
    if ll.instance.head.data is not None:
        assert ll.instance.search(ll.first).data == ll.first


def test_remove(ll):
    if ll.instance.head.data is not None:
        assert ll.instance.remove(ll.first).tail.data == ll.seq[1]


@pytest.mark.parametrize(
    'list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS
    )
def test_data_integrity(
    list_data, length, head_data, next_n_data, display, rem_val
):
    l_list = LinkedList(list_data)
    assert l_list.length == length
    assert l_list.head.data == head_data
    if l_list.head.data is not None:
        assert l_list.head.next_node.data == next_n_data


@pytest.mark.parametrize(
    'list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS
    )
def test_size(list_data, length, head_data, next_n_data, display, rem_val):
    l_list = LinkedList(list_data)
    assert l_list.size() == length


@pytest.mark.parametrize(
    'list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS
    )
def test_display(list_data, length, head_data, next_n_data, display, rem_val):
    l_list = LinkedList(list_data)
    assert l_list.display() == display


@pytest.mark.parametrize(
    'list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS
    )
def test_pop(list_data, length, head_data, next_n_data, display, rem_val):
    l_list = LinkedList(list_data)
    assert l_list.pop() == head_data


@pytest.mark.parametrize(
    'list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS
    )
def test_push(list_data, length, head_data, next_n_data, display, rem_val):
    l_list = LinkedList(list_data)
    l_list.push(8)
    assert l_list.head.data == 8
    assert l_list.size() == length + 1


@pytest.mark.parametrize(
    'list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS
    )
def test_remove(list_data, length, head_data, next_n_data, display, rem_val):
    l_list = LinkedList(list_data)
    x = l_list.search(rem_val)
    if x is not None and length > 0:
        assert l_list.remove(x).size() == length - 1
    else:
        assert l_list.remove(x).size() == length
