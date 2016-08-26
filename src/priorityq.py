# -*- coding: utf-8 -*-
"""This is a module for a priority queue.

A Priority Queue is similar to a queue, except that in addition to a
value, each QNode in the queue has a “priority”. When you pop a QNode
off of the queue, you always get the highest priority QNode.
"""


class QNode(object):
    """QNode class.

    Has data and a priority, with 0 indicating no/lowest priority, 1 
    indicating the highest, and priority decreasing as the number 
    increases.
    """

    def __init__(self, value=None, priority=0):
        """Initialize the Node instance.

        Highest priority is 1.  As the number increases, the priority
        goes down, with 0 indicating the lowest, or no priority.
        """
        if type(priority) != int or priority < 0:
            raise ValueError('Invalid priority value.')
        self.priority = priority
        self.value = value


    def __repr__(self):
        """Display the data in this node."""
        return repr((self.data, self.priority)


class PriorityQueue(object):
    """Priority queue class with insert, push and pop methods."""

    def __init__(self, queue=None):
        """Initialize the queue with optional queue(list).

        Only QNodes from the queue will be added to the Priority
        Queue."""
        self.queue = []
        try:
            for q in queue:
                if type(q) is QNode:
                    self.insert(q)
        except TypeError:
            if params is not None:
                raise TypeError('Expected list containing QNodes.')

    def __repr__(self):
        """Display the queue."""
        return repr(self.queue)

    def insert(self, n):
        """Insert an item(Qnode) into the queue."""
        pass

    def pop(self):
        """Pop the exit-node of the queue and return the value."""
        pass

    def peek(self):
        """Peek at the next item(node) value to be popped."""
        pass
