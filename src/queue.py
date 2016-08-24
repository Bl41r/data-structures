"""This is a module implementing stack class composed from LinkedList()."""

from dbl_lnk_lst import Dll


class Queue(object):
    """This is our Queue class and it's associated methods.

    The Queue class accepts an optional iterable as a parameter.
    """

    def __init__(self, iter=None):
        """Init instance of Queue."""
        self._queue = Dll(iter)
        self.size()

    def __repr__(self):
        """Represent self."""
        s = self._queue.__repr__()
        return str(s)

    def enqueue(self, val):
        """Push value onto teh stack."""
        self._queue.push(val)
        return self

    def dequeue(self):
        """Remove and return value from the queue."""
        if self.length > 0:
            val = self._queue.shift()
            return val
        else:
            raise IndexError('Cannot dequeue an empty queue.')

    def peek(self):
        """Peek at next value without dequeing it."""
        if self._queue.length > 0:
            return self._queue.tail.data
        else:
            return None

    def size(self):
        """Return size of queue."""
        current = self.head
        inc = 0
        while True:
            try:
                current = current.next_node
            except AttributeError:
                return inc
            inc += 1
