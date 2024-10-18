# /data_structures/graph.py
#
# Implementation of a Graph

class SimpleAdjacencyMatrixGraph:
    # Own first implementation of a graph
    def __init__(self, adjacency_matrix):
        self.a_m = adjacency_matrix

    def add_node(self, adjacency_row):
        if len(adjacency_row) == len(self.a_m) + 1:
            for i in range(len(self.a_m)):
                self.a_m[i].append(adjacency_row[i])
            self.a_m.append(adjacency_row)
        else:
            raise ValueError("Adjacency row is not the correct size.")

    def remove_node(self, number: int):
        if number < len(self.a_m):
            del self.a_m[number]
            for i in range(len(self.a_m)):
                del self.a_m[i][number]
        else:
            raise IndexError("Node index out of bounds.")

    def add_edge(self, node1: int, node2: int, weight: int = 1, directed: bool = False):
        if node1 < len(self.a_m) and node2 < len(self.a_m):
            self.a_m[node1][node2] = weight
            if not directed:
                self.a_m[node2][node1] = weight
        else:
            raise IndexError("Node indices out of bounds.")

    def remove_edge(self, node1: int, node2: int):
        if node1 < len(self.a_m) and node2 < len(self.a_m):
            self.a_m[node1][node2] = 0
            self.a_m[node2][node1] = 0
        else:
            raise IndexError("Node indices out of bounds.")

    def get_neighbors(self, node: int):
        if node >= len(self.a_m):
            raise IndexError("Node index out of bounds.")
        return [(i,w) for i, w in enumerate(self.a_m[node]) if w != 0]

    def __len__(self):
        return len(self.a_m)

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.a_m])


class SimpleAdjacencyListGraph:
    # Own first implementation of a graph
    def __init__(self, adjacency_list = None):
        if adjacency_list is None:
            self.a_l = {}
        else:
            self.a_l = adjacency_list

    def add_node(self, node: int) -> None:
        if node not in self.a_l:
            self.a_l[node] = set()
        else:
            raise ValueError("Node already exists in the graph.")

    def remove_node(self, node: int):
        if node in self.a_l:
            del self.a_l[node]
            for neighbors in self.a_l.values():
                neighbors.discard(node)
        else:
            raise ValueError("Node does not exist.")

    def add_edge(self, node1: int, node2: int, directed: bool = False):
        if node1 in self.a_l and node2 in self.a_l:
            self.a_l[node1].add(node2)
            if not directed:
                self.a_l[node2].add(node1)
        else:
            raise ValueError("Node indices out of bounds.")

    def remove_edge(self, node1: int, node2: int, directed: bool = False):
        if node2 in self.a_l[node1]:
            self.a_l[node1].remove(node2)
            if not directed:
                self.a_l[node2].remove(node1)
        else:
            raise ValueError("Node indices out of bounds.")

    def get_neighbors(self, node: int) -> set:
        if node not in self.a_l.keys():
            raise ValueError("Node index out of bounds.")
        return self.a_l[node]

    def __len__(self):
        return len(self.a_l)

    def __str__(self):
        result = []
        for node, neighbors in self.a_l.items():
            result.append(f"{node}: {neighbors}")
        return '\n'.join(result)

    def __contains__(self, node):
        return node in self.a_l

