# -*- coding: utf-8 -*-
"""This is a module for a priority queue.

A Priority Queue is similar to a queue, except that in addition to a
value, each item in the queue has a “priority”. When you pop an item
off of the queue, you always get the highest priority item.
"""


class PriorityQueue(object):
    """Min heap class with push and pop methods."""

    def __init__(self, heap=[]):
        """Initialize the heap with optional heap(list) of integers."""
        if type(heap) is not list:
            raise TypeError('Heap must be a list of integers.')

        try:
            self.heap = sorted(heap)
            for num in heap:
                self.push(int(num))
        except (ValueError, TypeError):
            raise TypeError('Heap must contain integers only.')

    def __repr__(self):
        """Display the heap in list form."""
        return repr(self.heap)

    def insert(self, n):
        """Insert0 an item into the queue."""
        pass

    def pop(self):
        """Pop the root of the tree and return the value."""
        pass

    def peek(self):
        """Peek at the next item to be popped."""
