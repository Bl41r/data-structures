# -*- coding: utf-8 -*-
"""Test of stack.py."""

import pytest
from stack import Stack

# format: (list of datas, length, head data, next node data, display, rem_val)
TEST_DATAS = [
    ([5, 4, 3, 2, 1], 5, 1, 2, '(1, 2, 3, 4, 5, None)', 3),
    (['z', 'y', 'x', 'w', 'v', 'u'], 6, 'u', 'v', "(u, v, w, x, y, z, None)", 'z'),
    ([], 0, None, None, '(None)', 2)
]


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS)
def test_data_integrity(list_data, length, head_data, next_n_data, display, rem_val):
    stack = Stack(list_data)
    assert stack._stack.length == length
    assert stack._stack.head.data == head_data
    if stack._stack.head.data is not None:
        assert stack._stack.head.next_node.data == next_n_data


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS)
def test_pop(list_data, length, head_data, next_n_data, display, rem_val):
    stack = Stack(list_data)
    assert stack.pop() == head_data


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS)
def test_push(list_data, length, head_data, next_n_data, display, rem_val):
    stack = Stack(list_data)
    stack.push(8)
    assert stack._stack.head.data == 8
    assert stack._stack.length == length + 1


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val', TEST_DATAS)
def test_display(list_data, length, head_data, next_n_data, display, rem_val):
    stack = Stack(list_data)
    assert stack.__repr__() == display
