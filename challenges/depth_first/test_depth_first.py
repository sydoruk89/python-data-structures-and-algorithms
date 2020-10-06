import pytest
from depth_first import Graph, Node

def test_breadth_1_edge():
    graph = Graph()
    first = graph.add_node('spam')
    second = graph.add_node('bacon')
    graph.add_edge(first, second)
    assert graph.depth_first(first) == ['spam', 'bacon']

def test_breadth_first_3_el():
    graph = Graph()
    start = graph.add_node('spam')
    middle = graph.add_node('bacon')
    end = graph.add_node('eggs')
    graph.add_edge(start, end)
    graph.add_edge(start, middle, 2)
    assert graph.depth_first(start) == ['spam', 'bacon', 'eggs']

def test_breadth_first_few_edges():
    graph = Graph()
    a = graph.add_node('A')
    b = graph.add_node('B')
    c = graph.add_node('C')
    g = graph.add_node('G')
    d = graph.add_node('D')
    e = graph.add_node('E')
    h = graph.add_node('H')
    f = graph.add_node('F')

    graph.add_edge(a, d)
    graph.add_edge(a, b)
    graph.add_edge(b, c)
    graph.add_edge(c, g)
    graph.add_edge(d, f)
    graph.add_edge(d, h)
    graph.add_edge(d, e)
    graph.add_edge(h, f)
    assert graph.depth_first(a) == ['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']