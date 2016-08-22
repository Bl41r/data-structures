# -*- coding: utf-8 -*-
"""Test of dbl_lnk_lst.py."""

import pytest
<<<<<<< HEAD
from dbl_lnk_lst import Dll
=======
>>>>>>> queue
from queue import Queue

# format:
# (list of datas,
# length,
# head data,
# shift val)


TEST_DATAS = [
    ([5, 4, 3, 2, 1], 5, 1, 5),
    (['z', 'y', 'x', 'w', 'v', 'u'], 6, 'u', 'z'),
    ([], 0, None, None)
]


@pytest.mark.parametrize('list_data, length, head_data, shift', TEST_DATAS)
def test_data(list_data, length, head_data, shift):
    q = Queue(list_data)
    print(q)
    assert q.length == length
    assert q._queue.head.data == head_data
    if q._queue.head.data is not None:
        assert q._queue.head.next_node.data == q._queue.head.next_node.data


@pytest.mark.parametrize('list_data, length, head_data, shift', TEST_DATAS)
def test_size(list_data, length, head_data, shift):
    q = Queue(list_data)
    assert q.size() == length


@pytest.mark.parametrize('list_data, length, head_data, shift', TEST_DATAS)
def test_enqueue(list_data, length, head_data, shift):
    q = Queue(list_data)
    assert q.enqueue(6).peek() == q.peek()


@pytest.mark.parametrize('list_data, length, head_data, shift', TEST_DATAS)
def test_dequeue(list_data, length, head_data, shift):
    q = Queue(list_data)
    if q is not None:
        assert q.dequeue() == shift
    else:
        q.dequeue() == IndexError


@pytest.mark.parametrize('list_data, length, head_data, shift', TEST_DATAS)
def test_peek(list_data, length, head_data, shift):
    q = Queue(list_data)
    if q._queue.length > 0:
        assert q.peek() == shift
    else:
        assert q.peek() is None
