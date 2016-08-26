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
                self.heap.append(int(num))
        except (ValueError, TypeError):
            raise TypeError('Heap must contain only integers.')

    def __repr__(self):
        """Display the heap in list form."""
        return repr(self.heap)

    def push(self, val):
        """Push an integer onto the heap."""
        try:
            self.head.append(int(val))
        except TypeError:
            raise TypeError('Must push an integer value.')

    def pop(self):
        """Pop the root of the tree and return the value."""
        pass

    def swap(self, a, b):
        """Swap 2 values in heap."""
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def parent_index(self, child_idx):
        """Return index of parent. Negative 1 indicates idx is root."""
        return int(child_idx + 1 // 2) - 1

    def first_child(self, parent_idx):
        """Return index of left child."""
        return 2 * parent_idx + 1

"""
             0
          1     3
        2   5  4  7  ---> Pop   1
                               0 3
                              2 54 7 --->
                                            1
                                           2  3
                                          0 54 7 ---> 1
                                                     2 3
                                                    54 7
"""
