import pytest
from graph import Graph
from get_edge import get_edge

def test_list_of_cities_is_empty():
    graph = Graph()
    city_1 = graph.add_node('Seattle')
    city_2 = graph.add_node('Portland')
    graph.add_edge(city_1, city_2, 150)
    assert get_edge(graph, []) == 'False, $0'

def test_one_city():
    graph = Graph()
    city_1 = graph.add_node('Seattle')
    city_2 = graph.add_node('Portland')
    graph.add_edge(city_1, city_2, 150)
    assert get_edge(graph, [city_1]) == 'False, $0'

def test_two_cities():
    graph = Graph()
    city_1 = graph.add_node('Seattle')
    city_2 = graph.add_node('Portland')
    city_3 = graph.add_node('San')
    graph.add_edge(city_1, city_2, 150)
    graph.add_edge(city_2, city_3, 200)
    assert get_edge(graph, [city_1, city_2]) == 'True, $150'

def test_4_cities():
    graph = Graph()
    city_1 = graph.add_node('Seattle')
    city_2 = graph.add_node('Portland')
    city_3 = graph.add_node('San')
    city_4 = graph.add_node('LA')
    graph.add_edge(city_1, city_2, 150)
    graph.add_edge(city_2, city_3, 200)
    graph.add_edge(city_3, city_4, 300)
    assert get_edge(graph, [city_1, city_2, city_3, city_4]) == 'True, $650'

def test_circle():
    graph = Graph()
    city_1 = graph.add_node('Seattle')
    city_2 = graph.add_node('Portland')
    city_3 = graph.add_node('San')
    graph.add_edge(city_1, city_2, 150)
    graph.add_edge(city_2, city_3, 200)
    graph.add_edge(city_3, city_1, 300)
    assert get_edge(graph, [city_1, city_2, city_3, city_1]) == 'True, $650'

def test_circle_false():
    graph = Graph()
    city_1 = graph.add_node('Seattle')
    city_2 = graph.add_node('Portland')
    city_3 = graph.add_node('San')
    city_4 = graph.add_node('LA')
    graph.add_edge(city_1, city_2, 150)
    graph.add_edge(city_2, city_3, 200)
    graph.add_edge(city_3, city_1, 300)
    assert get_edge(graph, [city_1, city_2, city_4]) == 'False, $0'

def test_circle_false_2():
    graph = Graph()
    city_1 = graph.add_node('Seattle')
    city_2 = graph.add_node('Portland')
    city_3 = graph.add_node('San')
    city_4 = graph.add_node('LA')
    graph.add_edge(city_1, city_2, 150)
    graph.add_edge(city_1, city_3, 200)
    graph.add_edge(city_3, city_4, 300)
    assert get_edge(graph, [city_1, city_3, city_4]) == 'True, $500'

def test_2_way(): 
    graph = Graph()
    city_1 = graph.add_node('Seattle')
    city_2 = graph.add_node('Portland')
    city_3 = graph.add_node('San')
    city_4 = graph.add_node('LA')
    graph.add_edge(city_1, city_2, 150)
    graph.add_edge(city_1, city_3, 200)
    graph.add_edge(city_2, city_1, 150)
    assert get_edge(graph, [city_1, city_2, city_1]) == 'True, $300'