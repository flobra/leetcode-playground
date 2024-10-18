# /algorithms/graph/bfs.py

from data_structures.graph import SimpleAdjacencyMatrixGraph
from data_structures.queue import CircularBufferQueue

def breadth_first_search(g: SimpleAdjacencyMatrixGraph, s: int):

    if s >= len(g.a_m):
        raise IndexError("Starting node index out of bounds.")

    # Initialize all the data structures needed for the task
    visited = set()
    queue = CircularBufferQueue()

    visited.add(s)
    queue.enqueue(s)

    while(not queue.is_empty()):
        curr = queue.dequeue()
        for neighbor in g.get_neighbors(curr):
            neighbor_node = neighbor[0]
            if neighbor_node not in visited:
                visited.add(neighbor_node)
                queue.enqueue(neighbor_node)

    return visited
