# -*- coding: utf-8 -*-
"""This is a module for a binary heap.

It uses a list to maintain the values and their relationships.  Use push
to insert a value into the heap, and pop to remove and return the root.
"""


class MinHeap(object):
    """Min heap class with push and pop methods."""

    def __init__(self, heap=[]):
        """Initialize the heap with optional heap(list) of integers."""
        if type(heap) is not list:
            raise TypeError('Heap argument must be list type.')

        try:
            self.heap = sorted(heap)
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
            return None

        if left < right:
            return left_index
        if right <= left:
            return left_index + 1

    def _get_last_index_top(self, l):
        """Get last index before final branch layer.

        Future:  use math, still working on formula.
        """
        n = 1
        while l > n - 1:
            t = n - 1
            n *= 2
        return t - 1

    # User methods
    def push(self, val):
        """Push an integer onto the heap."""
        try:
            self.heap.append(int(val))
        except TypeError:
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
            popped_val = self.heap[0]
        except IndexError:
            raise IndexError('Cannot pop an empty heap.')
        popped_idx = 0
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        last_index_top = self._get_last_index_top(len(self.heap))

        while popped_idx <= last_index_top:
            try:
                min_child_idx = self._min_child(popped_idx)
                self._swap(popped_idx, min_child_idx)
                popped_idx = min_child_idx
            except TypeError:
                self._swap(popped_idx, last_index_top + 1)
                popped_idx = last_index_top + 1
                break

        return popped_val
