"""Implementation ofa link-list data type in Python."""

class LinkedList(object):
    
    def __init__(self, node_list):
        self.node_list = node_list
        self.linked_list = {}
        for index, node in enumerate(reversed(node_list)):
            print(node)
            self.linked_list[node] = self.linked_list[node]
        print(self.linked_list)
