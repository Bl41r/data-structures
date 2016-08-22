import pytest
from linked_list import Node, LinkedList


@pytest.fixture(scope="function")
def _Node():
    return Node(1)


@pytest.fixture(scope="function")
def _ll():
    return LinkedList(['1', 'a', '2b', 'abc', 3, 4])


@pytest.fixture(scope="function")
def _ll1():
    return LinkedList(1)


@pytest.fixture(scope="function")
def _ll_None():
    return LinkedList()

ll_list = [
    ['1', 'a', '2b', 'abc', 3, 4],
    'abc',
    1,
    [],
    list(range(100))
    ]


@pytest.fixture(scope="function", params=ll_list)
def all_fix(request):
    result = {
        'instance': LinkedList(request.param),
        'pop_value': request.param[-1],
        'push_value': 0
    }
    return result
