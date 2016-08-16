# -*- encoding: utf-8 -*-
'''This is a module implementing a stack function composed from LinkedList()'''


from linked_list import LinkedList


class Stack(object, idx=None):
    def __init__(self, idx):
        self._container = LinkedList(idx)

    def push(self, val):
        self._container.push(val)

    def pop(self):
        self._container.pop()
