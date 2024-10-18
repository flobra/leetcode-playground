# tests/test_algorithms/test_dfs.py
import pytest
from data_structures.graph import SimpleAdjacencyListGraph
from algorithms.graph.dfs import iterative_dfs, recursive_dfs

@pytest.fixture
def simple_graph():
    g = SimpleAdjacencyListGraph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    return g

@pytest.fixture
def disconnected_graph():
    g = SimpleAdjacencyListGraph()
    g.add_node(0)
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(3, 4)
    return g

@pytest.fixture
def single_node_graph():
    g = SimpleAdjacencyListGraph()
    g.add_node(0)
    return g

@pytest.fixture
def empty_graph():
    return SimpleAdjacencyListGraph()

def test_iterative_dfs_simple_graph(simple_graph):
    result = iterative_dfs(simple_graph, 0)
    assert result == [0, 1, 3, 2, 4]

def test_recursive_dfs_simple_graph(simple_graph):
    visit_order = []
    visited = {}
    recursive_dfs(simple_graph, visited, visit_order, 0)
    assert visit_order == [0, 1, 3, 2, 4]

def test_iterative_dfs_disconnected_graph(disconnected_graph):
    result = iterative_dfs(disconnected_graph, 0)
    assert result == [0, 1, 2]

    result = iterative_dfs(disconnected_graph, 3)
    assert result == [3, 4]

def test_recursive_dfs_disconnected_graph(disconnected_graph):
    visit_order = []
    visited = {}
    recursive_dfs(disconnected_graph, visited, visit_order, 0)
    assert visit_order == [0, 1, 2]

    visit_order = []
    visited = {}
    recursive_dfs(disconnected_graph, visited, visit_order, 3)
    assert visit_order == [3, 4]

def test_iterative_dfs_single_node(single_node_graph):
    result = iterative_dfs(single_node_graph, 0)
    assert result == [0]

def test_recursive_dfs_single_node(single_node_graph):
    visit_order = []
    visited = {}
    recursive_dfs(single_node_graph, visited, visit_order, 0)
    assert visit_order == [0]

def test_iterative_dfs_empty_graph(empty_graph):
    with pytest.raises(ValueError, match="Start node not in graph."):
        iterative_dfs(empty_graph, 0)

def test_recursive_dfs_empty_graph(empty_graph):
    with pytest.raises(ValueError, match="Start node not in graph."):
        visit_order = []
        visited = {}
        recursive_dfs(empty_graph, visited, visit_order, 0)

