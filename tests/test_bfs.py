# tests/test_bfs.py
import pytest
from algorithms.graph.bfs import breadth_first_search
from data_structures.graph import SimpleAdjacencyGraph

def test_bfs_simple_graph():
    g = SimpleAdjacencyGraph([[1, 1, 0], [1, 0, 1], [0, 0, 1]])
    assert breadth_first_search(g, 0) == {0, 1, 2}  # Should visit all nodes

def test_bfs_larger_graph():
    h = SimpleAdjacencyGraph([[0, 1, 0, 1, 0, 1, 0],
                              [1, 0, 1, 1, 0, 0, 0],
                              [0, 1, 0, 1, 0, 0, 0],
                              [1, 1, 1, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0],
                              [1, 0, 0, 0, 0, 0, 1],
                              [0, 0, 0, 0, 0, 1, 0]])
    assert breadth_first_search(h, 0) == {0, 1, 3, 2, 5, 6}  # Should visit nodes connected to 0

def test_bfs_disconnected_graph():
    g = SimpleAdjacencyGraph([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    assert breadth_first_search(g, 0) == {0, 1}  # Node 2 is disconnected

def test_bfs_empty_graph():
    g = SimpleAdjacencyGraph([])
    with pytest.raises(IndexError):
        breadth_first_search(g, 0)  # Should raise an error due to invalid start node

def test_bfs_single_node_graph():
    g = SimpleAdjacencyGraph([[1]])  # A single node with a self-loop
    assert breadth_first_search(g, 0) == {0}

def test_bfs_starting_node_out_of_bounds():
    g = SimpleAdjacencyGraph([[1, 1, 0], [1, 0, 1], [0, 0, 1]])
    with pytest.raises(IndexError):
        breadth_first_search(g, 3)  # Starting node is out of bounds

def test_bfs_directed_graph():
    g = SimpleAdjacencyGraph([[0, 1, 0], [0, 0, 1], [0, 0, 0]])  # Directed graph
    assert breadth_first_search(g, 0) == {0, 1, 2}  # Should visit nodes following directed edges

def test_bfs_no_edges_graph():
    g = SimpleAdjacencyGraph([[0, 0, 0], [0, 0, 0], [0, 0, 0]])  # No connections
    assert breadth_first_search(g, 0) == {0}  # Only the start node should be visited

def test_bfs_weighted_graph():
    g = SimpleAdjacencyGraph([[0, 2, 0], [2, 0, 3], [0, 3, 0]])  # Weighted graph
    assert breadth_first_search(g, 0) == {0, 1, 2}  # BFS should still find all nodes

def test_bfs_cyclic_graph():
    g = SimpleAdjacencyGraph([[0, 1, 0, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, 0, 1, 0]])  # 4 nodes in a cycle
    assert breadth_first_search(g, 0) == {0, 1, 2, 3}  # All nodes should be visited without infinite loop

def test_bfs_isolated_node():
    g = SimpleAdjacencyGraph([[0, 1, 0], [1, 0, 0], [0, 0, 0]])  # Node 2 is isolated
    assert breadth_first_search(g, 2) == {2}  # BFS should only visit the isolated node itself

def test_bfs_from_middle_node():
    g = SimpleAdjacencyGraph([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    assert breadth_first_search(g, 1) == {0, 1, 2}  # Starting from middle node visits all
