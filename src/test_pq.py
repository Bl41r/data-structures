# -*- coding: utf-8 -*-

"""This is the test file for the priority queue module. Expected behavior below:"""

from __future__ import unicode_literals
from collections import namedtuple
import pytest
import random
import string
import itertools

'''

'''


EDGE_CASES = [
    {},
    [],
    {'a': 0},
    [1, 2, 3],
    'Æ',
    ''
]

INT_CASES = [random.sample(range(1000),
             random.randrange(5, 100)) for n in range(10)
             ]


STR_CASES = [random.sample(string.printable,
             random.randrange(2, 100)) for n in range(10)
             ]

TEST_CASES = EDGE_CASES + INT_CASES + STR_CASES

MyPQFix = namedtuple(
    'pqFixture',
    ('pqueue', 'input_val', 'len_int_list', 'type_err', 'int_list_priority')
)


@pytest.fixture(scope='function', params=TEST_CASES)
def pq(request):
    '''return an empty Priority Queue'''
    from priorityq import PriorityQueue
    pqueue = PriorityQueue()
    input_val = None
    int_list_priority = []
    if type(request.param) is int:
        for val in request.param:
            int_list_priority.append(val)
    type_err = None
    if type(request.param) is not str():
        type_err = TypeError
    for val in request.param:
        try:
            input_val = val
        except:
            pass
    len_int_list = len(int_list_priority)
    int_list_priority = sorted(int_list_priority)
    return MyPQFix(pqueue,
                   input_val,
                   len_int_list,
                   type_err,
                   int_list_priority
                   )

# Test PNode creation


def test_node_init(pq):
    from priorityq import PNode
    try:
        a = PNode(pq.input_val, pq.input_val)
        assert a.value == pq.input_val
    except ValueError:
        with pytest.raises(ValueError):
            PNode(pq.input_val, pq.input_val)

# Test PriorityQueue public functions


def test_insert_non_list_error(pq):
    """
    Confirm that attempting to initialize a PriorityQueue with anything but a
    a list throws a TypeError
    """
    with pytest.raises(TypeError):
        pq.pqueue(pq.input_val)


def test_instantiate_list_non_PNodes(pq):
    """
    Confirm that attempting to initialize a PriorityQueue with anything but a
    a list of PNodes throws a TypeError
    """
    with pytest.raises(TypeError):
        pq.pqueue(pq.int_list_priority)


def test_insert_nonnode(pq):
    """
    Confirm that attempting to insert anything buy a PNode type
    throws a TypeError
    """
    with pytest.raises(TypeError):
        pq.pqueue.insert(pq.input_val)


def test_insert_node(pq):
    """
    Confirm that the insert functions adds PNodes to the PriorityQueue and
    sorts them properly regardless of order of insert.
    """
    from priorityq import PNode
    if type(pq.input_val) is int:
        a = PNode('a', pq.input_val)
        b = PNode('b', pq.input_val * 2)
        c = PNode('c', pq.input_val * 3)
        d = PNode('d', pq.input_val * 4)
        e = PNode('e', pq.input_val * 5)
        pq.pqueue.insert(e)
        pq.pqueue.insert(c)
        pq.pqueue.insert(a)
        pq.pqueue.insert(d)
        pq.pqueue.insert(b)
        assert pq.pqueue.heap[0] == a


def test_empty_pqueue(pq):
    with pytest.raises(IndexError):
        pq.pqueue.pop()


def test_pqueue_one_node_pop_2x(pq):
    """Add one item to a pq, then pop twice, make sure error raised."""
    from priorityq import PNode
    if type(pq.input_val) is int:
        a = PNode('a', pq.input_val)
        pq.pqueue.insert(a)
        pq.pqueue.pop()
        with pytest.raises(IndexError):
            pq.pqueue.pop()


def test_pqueue_one_node_pop_peek(pq):
    """Add one item to a pq, then pop and assert peek is None."""
    from priorityq import PNode
    if type(pq.input_val) is int:
        a = PNode('a', pq.input_val)
        pq.pqueue.insert(a)
        pq.pqueue.pop()
        assert pq.pqueue.peek() is None


def test_pqueue_with_one_item_in_sequence(pq):
    """Add one item to a list, then create Pqueue and check length."""
    from priorityq import PNode, PriorityQueue
    if type(pq.input_val) is int:
        a = PNode('a', pq.input_val)
        new_heap = [a]
        pq1 = PriorityQueue(new_heap)
        assert len(pq1.heap) == 1


def test_pqueue_with_tuple_input(pq):
    """Test TypeError raised when using tuple instead of list."""
    from priorityq import PNode, PriorityQueue
    if type(pq.input_val) is int:
        a = PNode('a', pq.input_val)
        new_heap = (a)
        with pytest.raises(TypeError):
            pq1 = PriorityQueue(new_heap)


def test_pqueue_with_list_non_PNodes():
    """Test TypeError raised with list of non-PNodes."""
    from priorityq import PriorityQueue
    new_heap = [1, 2, 3, 'hi']
    with pytest.raises(TypeError):
        pq1 = PriorityQueue(new_heap)


def test_equal_priorities():
    """Assert order is by when inserted with equal priorities."""
    from priorityq import PNode, PriorityQueue
    a = PNode(1, 0)
    b = PNode(2, 0)
    c = PNode(3, 0)
    pq1 = PriorityQueue()
    pq1.insert(b)
    pq1.insert(a)
    pq1.insert(c)
    print(pq1.heap)
    assert pq1.pop() == b.value

def test_pop_node(pq):
    """
    Confirm that the insert functions adds PNodes to the PriorityQueue and
    sorts them properly regardless of order of insert.
    """
    from priorityq import PNode
    if type(pq.input_val) is int:
        a = PNode('a', pq.input_val)
        b = PNode('b', pq.input_val * 2)
        c = PNode('c', pq.input_val * 3)
        d = PNode('d', pq.input_val * 4)
        e = PNode('e', pq.input_val * 5)
        pq.pqueue.insert(e)
        pq.pqueue.insert(c)
        pq.pqueue.insert(a)
        pq.pqueue.insert(d)
        pq.pqueue.insert(b)
        assert pq.pqueue.pop() == a.value


def test_peek_empty_error(pq):
    pq.pqueue.peek() is None


def test_peek(pq):
    """
    Confirm that the peek function returns the highest priority node.
    """
    from priorityq import PNode
    if type(pq.input_val) is int:
        a = PNode('a', pq.input_val)
        b = PNode('b', pq.input_val * 2)
        c = PNode('c', pq.input_val * 3)
        d = PNode('d', pq.input_val * 4)
        e = PNode('e', pq.input_val * 5)
        pq.pqueue.insert(e)
        pq.pqueue.insert(c)
        pq.pqueue.insert(a)
        pq.pqueue.insert(d)
        pq.pqueue.insert(b)
        assert pq.pqueue.peek() == a
