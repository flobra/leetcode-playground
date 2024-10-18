# /data_structures/graph.py
#
# Implementation of a Graph

class SimpleAdjacencyGraph:
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

    def add_vertex(self, node1: int, node2: int, weight: int = 1, directed: bool = False):
        if node1 < len(self.a_m) and node2 < len(self.a_m):
            self.a_m[node1][node2] = weight
            if not directed:
                self.a_m[node2][node1] = weight
        else:
            raise IndexError("Node indices out of bounds.")

    def remove_vertex(self, node1: int, node2: int):
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

