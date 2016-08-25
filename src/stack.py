# -*- encoding: utf-8 -*-
"""This is a module implementing stack class composed from LinkedList()."""


from linked_list import LinkedList


class Stack(object):
    """This is our Stack class and it's associated methods.

    The Stack class accepts an optional iterable as a parameter.
    """

    def __init__(self, iter=None):
        """Initialize Stack."""
        self._stack = LinkedList(iter)

    def __repr__(self):
        """Representation of stack."""
        return u'(' + str(self._stack.head) + u')'

    def push(self, val):
        """Push a value onto the stack."""
        self._stack.push(val)

    def pop(self):
        """Pop head from stack and return value."""
        return self._stack.pop()
