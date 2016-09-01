# -*- coding: utf-8 -*-
"""This is a module for a priority queue.

A Priority Queue is similar to a queue, except that in addition to a
value, each PNode in the queue has a “priority”. When you pop a PNode
off of the queue, you always get the highest priority PNode.
"""


class PNode(object):
    """PNode class.

    Has data and a priority, with a lower number indicating indicating
    the highest, and priority decreasing as the number
    increases.
    """

    def __init__(self, value=None, priority=0):
        """Initialize the Node instance.

        As the number(int) increases, the priority
        goes down.
        """
        if type(priority) != int:
            raise ValueError('Invalid priority value.')
        self.priority = priority
        self.value = value

    def __repr__(self):
        """Display the data in this node."""
        return "({},{})".format(self.value, self.priority)


class PriorityQueue(object):
    """Priority queue class with insert, peek, and pop methods."""

    def __init__(self, heap=None):
        """Initialize the heap with optional queue(list) of PNodes."""
        if type(heap) is not list and heap is not None:
            raise TypeError('Heap argument must be list type.')

        if heap is None:
            self.heap = []
        else:
            self.heap = heap

        def getkey(item):
            return item.priority

        try:
            self.heap = sorted(self.heap, key=getkey)
        except (ValueError, TypeError):
            raise TypeError('Heap must contain only PNodes.')

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

        if (left.priority) < (right.priority):
            return left_index
        if (right.priority) <= (left.priority):
            return left_index + 1

    # User methods
    def insert(self, pnode):
        """Push a PNode onto the heap."""
        if type(pnode) is PNode:
            self.heap.append(pnode)
        else:
            raise TypeError('Must push a PNode type.')

        length = len(self.heap)
        new_val_idx = length - 1
        parent_idx = self._parent_index(new_val_idx)

        while True:
            if pnode.priority <= self.heap[parent_idx].priority and new_val_idx != 0:
                self._swap(parent_idx, new_val_idx)
                new_val_idx = parent_idx
                parent_idx = self._parent_index(new_val_idx)
            else:
                break

    def pop(self):
        """Pop the root of the tree and return the PNode value."""
        try:
            self._swap(0, -1)
            popped_val = self.heap.pop()
        except IndexError:
            raise IndexError('Cannot pop an empty heap.')
        curr_idx = 0

        while self._min_child(curr_idx) is not None and self.heap[self._min_child(curr_idx)].priority < self.heap[curr_idx].priority:
            min_child_idx = self._min_child(curr_idx)
            self._swap(curr_idx, min_child_idx)
            curr_idx = min_child_idx

        return popped_val

    def peek(self):
        """Peek at the next item(PNode) to be popped."""
        try:
            return self.heap[0]
        except IndexError:
            return None
