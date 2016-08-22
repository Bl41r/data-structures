from dbl_lnk_lst import Dll


class Deque(object):
    """This is our Queue class and it's associated methods.

    The Queue class accepts an optional iterable as a parameter.
    """

    def __init__(self, iter=None):
        self._queue = Dll(iter)
        self.length = self.size()

    def __repr__(self):
        s = self._queue.__repr__()
        return str(s)

    def appendleft(self, val):      # this was enqueue(val)
        """Push value onto the deque head."""
        self._queue.push(val)
        self.length += 1
        return self

    def append(self, val):
        """Append value to end of deque."""
        pass

    def pop(self):  # this was dequeue()
        """Remove and return value from the deque and return it."""
        try:
            val = self._queue.shift()
            self.length -= 1
            return val
        except AttributeError:
            raise IndexError('Cannot dequeue an empty queue.')
            pass

    def popleft(self):
        """Remove and return value from front of deque."""

    def peek(self):
        """Peek at next value without dequeing it."""
        if self._queue.length > 0:
            return self._queue.tail.data
        else:
            return None

    def peekleft(self):
        """Peek at front of dequeue without dequeing it."""
        pass

    def size(self):
        """Return size of deque."""
        return self._queue.length
