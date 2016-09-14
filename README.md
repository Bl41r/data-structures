# data-structures

Repo that holds implementations of a variety of data structures, including nodes, linked lists, double linked lists, stacks, and queues.

This branch features a graph with weighted edges.

#### methods
.insert(item): inserts an item into the queue.
.pop(): removes the most important item from the queue.
.peek(): returns the most important item without removing it from the queue.

This branch features the graph data type
- g.nodes(): return a list of all nodes in the graph
- g.edges(): return a list of all edges in the graph
- g.add_node(n): adds a new node ‘n’ to the graph
- g.add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added.
- g.del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
- g.del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
- g.has_node(n): True if node ‘n’ is contained in the graph, False if not.
- g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
- g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g


- g.depth_first_traversal(start): Perform a full depth-first traversal of the graph beginning at start. Return the full visited path when traversal is complete.
- g.breadth_first_traversal(start): Perform a full breadth-first traversal of the graph, beginning at start. Return the full visited path when traversal is complete.
- g.weight(n1, n2): Returns the weight of the edge connected two nodes