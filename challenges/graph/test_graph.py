import pytest
from graph import Graph, Node


def test_add_graph():
    graph = Graph()
    assert graph


def test_add_vertex():
    graph = Graph()
    node = graph.add_node('spam')
    assert node.value == 'spam'


def test_add_edge():
    graph = Graph()
    spam = graph.add_node('spam')
    egg = graph.add_node('eggs')
    graph.add_edge(spam, egg)
    assert True



def test_add_edge_test():
    graph = Graph()
    start = graph.add_node('start_vertex')
    end = graph.add_node('end_vertex')
    graph.add_edge(start, end)
    assert graph.adjacency_list[start][0].node == end


def test_add_edge_test_size_pass():
    graph = Graph()
    spam = graph.add_node('spam')
    egg = graph.add_node('eggs')
    graph.add_edge(spam, egg)
    assert len(graph.adjacency_list) == 2


def test_add_edge_test_size_fail():
    graph = Graph()
    spam = graph.add_node('spam')
    egg = graph.add_node('eggs')
    graph.add_edge(spam, egg)
    assert len(graph.adjacency_list) != 3

def test_get_nodes():
    graph = Graph()
    spam = graph.add_node('spam')
    egg = graph.add_node('eggs')
    assert graph.get_nodes() == {'spam', 'eggs'}

def test_neighbors_edges():
    graph = Graph()
    start = graph.add_node('spam')
    middle = graph.add_node('bacon')
    end = graph.add_node('eggs')
    graph.add_edge(start, end)
    graph.add_edge(start, middle, 2)
    assert graph.get_neighbors(start) == [1, 2]