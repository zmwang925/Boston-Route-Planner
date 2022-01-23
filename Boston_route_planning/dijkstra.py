
def find_lowest_cost_node(costs,processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:  
        cost = costs[node]
        if cost < lowest_cost and node not in processed: 
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def dijkstra(costs,parents,source,graph,destination):
    node = source
    processed = [source]
    while node is not None:   
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:  
                costs[n] = new_cost  
                parents[n] = node
        
        if node == destination:
            break

        node = find_lowest_cost_node(costs,processed)
        processed.append(node)
        
def initialize_node_distance(way_node_dic, source,graph,costs):
    infinity = float("inf")
    costs[source] = 0
    visited_node = [source]
    for des,dis in graph[source].items():
        costs[des] = dis
        visited_node.append(des)
    for key in way_node_dic.keys():
        if key not in visited_node:
            costs[key] = infinity
    

def initialize_node_parents(way_node_dic,source,graph,parents):
    
    parents[source] = None
    visited_node = []
    for key in graph[source].keys():
        parents[key] = source
        visited_node.append(key)
    for key in way_node_dic:
        if key not in visited_node:
            parents[key] = None
    

def find_shortest_path(parents,source,destination):
    node = destination
    shortest_path = [destination]
    while parents[node] != source:
        shortest_path.append(parents[node])
        node = parents[node]
    shortest_path.append(source)
    shortest_path.reverse()  
    return shortest_path
 