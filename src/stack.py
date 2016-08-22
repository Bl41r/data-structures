# -*- encoding: utf-8 -*-
"""This is a module implementing stack class composed from LinkedList()."""


from linked_list import LinkedList


class Stack(object):
    """This is our Stack class and it's associated methods.

    The Stack class accepts an optional iterable as a parameter.
    """

    def __init__(self, idx=None):
        self._stack = LinkedList(idx)

    def __repr__(self):
        s = self._stack.__repr__()
        return str(s)

    def push(self, val):
        """Push a value onto the stack."""
        self._stack.push(val)

    def pop(self):
        """Pop head from stack and return value."""
        return self._stack.pop()
