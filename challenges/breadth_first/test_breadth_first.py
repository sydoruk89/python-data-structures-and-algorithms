import pytest
from breadth_first import Graph, Node

def test_breadth_1_edge():
    graph = Graph()
    first = graph.add_node('spam')
    second = graph.add_node('bacon')
    graph.add_edge(first, second)
    assert graph.breadth_first(first) == ['spam', 'bacon']

def test_breadth_first_3_el():
    graph = Graph()
    start = graph.add_node('spam')
    middle = graph.add_node('bacon')
    end = graph.add_node('eggs')
    graph.add_edge(start, end)
    graph.add_edge(start, middle, 2)
    assert graph.breadth_first(start) == ['spam', 'eggs', 'bacon']

def test_breadth_first_few_edges():
    graph = Graph()
    first = graph.add_node('spam')
    second = graph.add_node('bacon')
    third = graph.add_node('eggs')
    fourth = graph.add_node('butter')
    graph.add_edge(first, second)
    graph.add_edge(first, third, 2)
    graph.add_edge(second, third, 3)
    graph.add_edge(third, fourth, 4)
    assert graph.breadth_first(first) == ['spam', 'bacon', 'eggs', 'butter']