'''This is a module implementing a stack function composed from LinkedList()'''


from dbl_lnk_lst import Dll


class Queue(object):
    '''
    This is our Queue class and it's associated methods.
    The Queue class accepts an optional iterable as a parameter.
    '''

    def __init__(self, iter=None):
        self._queue = Dll(iter)
        self.length = self.size()

    def __repr__(self):
        s = self._queue.__repr__()
        return str(s)

    def enqueue(self, val):
        self._queue.push(val)
        self.length += 1
        return self

    def dequeue(self):
        try:
            self._queue.shift()
            self.length += 1
            return self
        except AttributeError:
            raise IndexError('Cannot dequeue an empty queue.')
            pass

    def peek(self):
        return self._queue.tail

    def size(self):
        return self._queue.length
