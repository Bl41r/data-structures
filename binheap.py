# -*- coding: utf-8 -*-
"""This is a module for a binary heap.

It uses a list to maintain the values and their parent-child
relationships.
"""


class MinHeap(object):
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

    def push(self, val):
        """Push an integer onto the heap."""
        pass

    def pop(self):
        """Pop the root of the tree and return the value."""
        pass
