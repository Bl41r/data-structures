# -*- coding: utf-8 -*-
"""This is a module for a binary heap.

It uses a list to maintain the values and their relationships.  Use push
to insert a value into the heap, and pop to remove and return the root.
"""


class MinHeap(object):
    """Min heap class with push and pop methods."""

    def __init__(self, heap=None):
        """Initialize the heap with optional heap(list) of integers."""
        if type(heap) is not list and heap is not None:
            raise TypeError('Heap argument must be list type.')

        if heap is None:
            self.heap = []
        else:
            self.heap = heap

        try:
            self.heap = sorted(self.heap)
        except (ValueError, TypeError):
            raise TypeError('Heap must contain only integers.')

    def __repr__(self):
        """Display the heap in list form."""
        return repr(self.heap)

    # Internal methods
    def _swap(self, a, b):
        """Swap 2 values in heap."""
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def _parent_index(self, child_idx):
        """Return index of parent. Negative 1 indicates idx is root."""
        return ((child_idx - 1) // 2)

    def _min_child(self, parent_idx):
        """Return index of min child value."""
        left_index = 2 * parent_idx + 1
        try:
            left = self.heap[left_index]
        except IndexError:
            return None

        try:
            right = self.heap[left_index + 1]
        except IndexError:
            return left_index

        if left < right:
            return left_index
        if right <= left:
            return left_index + 1

    # User methods
    def push(self, val):
        """Push an integer onto the heap."""
        if isinstance(val, int):
            self.heap.append(val)
        else:
            raise TypeError('Must push an integer value.')
        length = len(self.heap)
        new_val_idx = length - 1
        parent_idx = self._parent_index(new_val_idx)

        while True:
            if val <= self.heap[parent_idx] and new_val_idx != 0:
                self._swap(parent_idx, new_val_idx)
                new_val_idx = parent_idx
                parent_idx = self._parent_index(new_val_idx)
            else:
                break

    def pop(self):
        """Pop the root of the tree and return the value."""
        try:
            self._swap(0, -1)
            popped_val = self.heap.pop()
        except IndexError:
            raise IndexError('Cannot pop an empty heap.')
        curr_idx = 0

        while self._min_child(curr_idx) is not None and self.heap[self._min_child(curr_idx)] < self.heap[curr_idx]:
            min_child_idx = self._min_child(curr_idx)
            self._swap(curr_idx, min_child_idx)
            curr_idx = min_child_idx

        return popped_val
