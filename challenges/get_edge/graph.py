class Graph:

    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, value):
        node = Node(value)
        self.adjacency_list[node] = []
        return node

    def add_edge(self, start, end, weight=1):
        # notion of checking if the node is in the graph start and the end
        if start not in self.adjacency_list:
            raise KeyError('Start Vertex not in the graph')
        if end not in self.adjacency_list:
            raise KeyError('End Vertex not in the graph')

        edge = Edge(end, weight)
        adjacencies = self.adjacency_list[start]
        adjacencies.append(edge)

    def size(self):
        return len(self.adjacency_list)

    def get_nodes(self):
        nodes = set()
        for el in self.adjacency_list:
            nodes.add(el.value)
        return nodes

    def get_neighbors(self, node):
        return [el.weight for el in self.adjacency_list[node]]


class Node:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, node, weight=1):
        self.node = node
        self.weight = weight
