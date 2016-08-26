# -*- coding: utf-8 -*-
"""This is a module for a priority queue.

A Priority Queue is similar to a queue, except that in addition to a
value, each item in the queue has a “priority”. When you pop an item
off of the queue, you always get the highest priority item.
"""

class 


class PriorityQueue(object):
    """Min heap class with push and pop methods."""

    def __init__(self, queue=None):
        """Initialize the heap with optional heap(list) of integers."""
        self.queue = queue

    def __repr__(self):
        """Display the heap in list form."""
        return repr(self.queue)

    def insert(self, n):
        """Insert an item into the queue."""
        pass

    def pop(self):
        """Pop the exit-node of the queue and return the value."""
        pass

    def peek(self):
        """Peek at the next item to be popped."""
        pass
