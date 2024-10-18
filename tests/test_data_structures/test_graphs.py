import pytest
from data_structures.graph import SimpleAdjacencyListGraph  # Replace with the actual module name

@pytest.fixture
def graph():
    """Fixture to create a graph instance before each test."""
    return SimpleAdjacencyListGraph()

def test_add_node(graph):
    graph.add_node(1)
    assert 1 in graph.a_l
    assert graph.a_l[1] == set()

    with pytest.raises(ValueError):
        graph.add_node(1)  # Adding an existing node should raise an error

def test_remove_node(graph):
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)

    graph.remove_node(1)
    assert 1 not in graph.a_l
    assert 2 in graph.a_l
    assert 1 not in graph.a_l[2]  # Node 1 should be removed from neighbors of 2

    with pytest.raises(ValueError):
        graph.remove_node(3)  # Removing a non-existing node should raise an error

def test_add_edge(graph):
    graph.add_node(1)
    graph.add_node(2)

    graph.add_edge(1, 2)
    assert 2 in graph.a_l[1]
    assert 1 in graph.a_l[2]  # Check undirected behavior by default

    graph.add_node(3)
    graph.add_edge(1, 3, directed=True)
    assert 3 in graph.a_l[1]
    assert 1 not in graph.a_l[3]  # Directed, so 3 should not have 1 as a neighbor

    with pytest.raises(ValueError):
        graph.add_edge(1, 4)  # Adding edge with non-existing node

def test_remove_edge(graph):
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)

	# Now remove it as a directed edge (should only remove one direction)
    graph.remove_edge(1, 2, directed=True)
    assert 2 not in graph.a_l[1]  # The edge from 1 to 2 should be removed
    assert 1 in graph.a_l[2]  # The reverse edge (2 -> 1) should still be there because it's undirected

    # Now remove the reverse edge (2 -> 1)
    graph.remove_edge(2, 1, directed=True)
    assert 1 not in graph.a_l[2]  # The edge from 2 to 1 should now be removed

    with pytest.raises(ValueError):
        graph.remove_edge(1, 3)  # Removing edge between non-existing nodes

def test_get_neighbors(graph):
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)

    assert graph.get_neighbors(1) == {2}
    assert graph.get_neighbors(2) == {1}

    with pytest.raises(ValueError):
        graph.get_neighbors(3)  # Getting neighbors of non-existing node

def test_len(graph):
    assert len(graph) == 0
    graph.add_node(1)
    assert len(graph) == 1
    graph.add_node(2)
    assert len(graph) == 2
    graph.remove_node(1)
    assert len(graph) == 1

def test_str(graph):
    graph.add_node(1)
    graph.add_node(2)
    graph.add_edge(1, 2)
    assert str(graph) == "1: {2}\n2: {1}"

def test_contains(graph):
    graph.add_node(1)
    assert 1 in graph
    assert 2 not in graph

    graph.add_node(2)
    assert 2 in graph

