# /algorithms/graph/dfs.py

from data_structures.graph import SimpleAdjacencyListGraph
from data_structures.stack import Stack

def iterative_dfs(g: SimpleAdjacencyListGraph, start: int):

    if start not in g:
        raise ValueError('Start node not in graph.')

    visited = set()
    visit_order = []
    stack = Stack()

    stack.push(start)

    while not stack.empty():
        curr = stack.pop()
        if curr not in visited:
            visited.add(curr)
            visit_order.append(curr)
            for neighbor in sorted(g.get_neighbors(curr), reverse = True):
                if neighbor not in visited:
                    stack.push(neighbor)

    return visit_order

def recursive_dfs(g: SimpleAdjacencyListGraph, visited: dict, visit_order: list, start: int):
    if start not in g:
        raise ValueError('Start node not in graph.')

    visited[start] = True
    visit_order.append(start)

    for neighbor in g.get_neighbors(start):
        if neighbor not in visited or not visited[neighbor]:
            recursive_dfs(g, visited, visit_order, neighbor)
