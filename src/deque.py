# -*- coding: utf-8 -*-
from dbl_lnk_lst import Dll


class Deque(object):
    """This is our Queue class and it's associated methods.

    The Queue class accepts an optional iterable as a parameter.
    """

    def __init__(self, iter=None):
        """Initialize the Deque."""
        self._deque = Dll(iter)

    def __repr__(self):
        """Show the Deque."""
        return repr(self._deque)

    def appendleft(self, val):      # this was enqueue(val)
        """Push value onto the deque head."""
        self._deque.push(val)
        return self

    def append(self, val):
        """Append value to end of deque."""
        self._deque.append(val)
        return self

    def pop(self):  # this was dequeue()
        """Remove and return value from the deque and return it."""
        val = self._deque.shift()
        return val

    def popleft(self):
        """Remove and return value from front of deque."""
        val = self._deque.pop()
        return val

    def peek(self):
        """Peek at next value without dequeing it."""
        return self._deque.tail.data

    def peekleft(self):
        """Peek at front of dequeue without dequeing it."""
        return self._deque.head.data


    def size(self):
        """Return size of deque."""
        return self._deque.size()
