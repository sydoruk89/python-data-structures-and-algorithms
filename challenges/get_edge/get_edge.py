from graph import Graph

def get_edge(graph, city_list):
    cost = 0
    l = len(city_list)
    if l == 1 or l == 0:
        trip = 'False'
    for i in range(l-1):
        for el in graph.adjacency_list[city_list[i]]:
            if el.node==city_list[i+1]:
                cost += el.weight
                trip = 'True'
                break
            else:
                trip = 'False'
                cost = 0
    return f'{trip}, ${str(cost)}'