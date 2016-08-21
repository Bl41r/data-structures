# -*- coding: utf-8 -*-
"""Test of linked-list.py."""

import pytest
from linked_list import LinkedList

# format: (list of datas, length, head data, next node data, display, rem_val)
TEST_DATAS = [
    ([5, 4, 3, 2, 1], 5, 1, 2, '(1, 2, 3, 4, 5, None)', 3),
    (['z', 'y', 'x', 'w', 'v', 'u'], 6, 'u', 'v', "(u, v, w, x, y, z, None)", 'z'),
    ([], 0, None, None, '(None)', 2)
]

TEST_LISTS = [(LinkedList(data[0]), data[1], data[2], data[3], data[4], data[5]) for data in TEST_DATAS]


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
