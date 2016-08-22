# -*- coding: utf-8 -*-
"""Test of dbl_lnk_lst.py."""

import pytest
from dbl_lnk_lst import Dll

# format: (list of datas, length, head data, next node data, display, rem_val, search, shift)
TEST_DATAS = [
    ([5, 4, 3, 2, 1], 5, 1, 2, '(1, 2, 3, 4, 5)', 3, 1, 5),
    (['z', 'y', 'x', 'w', 'v', 'u'], 6, 'u', 'v', "(u, v, w, x, y, z)", 'z', 'w', 'z'),
<<<<<<< HEAD
    ([], 0, None, None, '(None)', 2, None, None)
=======
    ([], 0, None, None, '(None)', 2, 1, None)
>>>>>>> stack
]


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_data_integrity(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    print(l_list)
    assert l_list.length == length
    assert l_list.head.data == head_data
    if l_list.head.data is not None:
        assert l_list.head.next_node.data == next_n_data


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_size(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    assert l_list.size() == length


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_display(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    assert l_list.display() == display


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_pop(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    assert l_list.pop() == head_data


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_push(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    l_list.push(8)
    assert l_list.head.data == 8
    assert l_list.size() == length + 1


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_shift(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    assert l_list.shift() == shift
<<<<<<< HEAD


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_length(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    if l_list:
        assert l_list.__len__() == length


@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_search(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    if l_list:
        assert l_list.search(l_list.head.data).data == l_list.head.data

@pytest.mark.parametrize('list_data, length, head_data, next_n_data, display, rem_val, search, shift', TEST_DATAS)
def test_remove(list_data, length, head_data, next_n_data, display, rem_val, search, shift):
    l_list = Dll(list_data)
    if l_list:
        assert l_list.remove(l_list.head.data) == (l_list.head, l_list, l_list.length)
=======
>>>>>>> stack
