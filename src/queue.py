"""This is a module implementing stack class composed from LinkedList()."""

from dbl_lnk_lst import Dll


class Queue(object):
    """This is our Queue class and it's associated methods.

    The Queue class accepts an optional iterable as a parameter.
    """

    def __init__(self, iter=None):
        self._queue = Dll(iter)
        self.length = self.size()

    def __repr__(self):
        s = self._queue.__repr__()
        return str(s)

    def enqueue(self, val):
        """Push value onto teh stack."""
        self._queue.push(val)
        self.length += 1
        return self

    def dequeue(self):
        """Remove and return value from the queue."""
        try:
            val = self._queue.shift()
            self.length -= 1
            return val
        except AttributeError:
            raise IndexError('Cannot dequeue an empty queue.')
            pass

    def peek(self):
        """Peek at next value without dequeing it."""
        if self._queue.length > 0:
            return self._queue.tail.data
        else:
            return None

    def size(self):
        """Return size of queue."""
        return self._queue.length
