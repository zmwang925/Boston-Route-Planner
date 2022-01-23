import json 
import heapdict
from geopy.distance import geodesic

#load vertices from json file
with open("new_way_node.json",'r', encoding='UTF-8') as f:
    nodes_dic = json.load(f)

#load edges from json file
with open("new_src_des.json",'r', encoding='UTF-8') as f:
    edges_dic = json.load(f)

def get_neighbors(node_id):
    neighbors = []
    for i,a in enumerate(edges_dic[node_id]):
        if i == 0:
            continue
        else:
            neighbors.append(a)
    return neighbors
 
#calculate distance between two vertex given latitudes and longitudes 
def distance(lon1, lat1, lon2, lat2): 
    return geodesic((lat1, lon1), (lat2, lon2)).km

class Node:
    def __init__(self,id,location,t_location,neighbors):
        self.d = 999
        self.id = id
        self.location = location
        self.neighbors = neighbors
        self.h = distance(lon1 = location[1],lat1 = location[0], lon2 = t_location[1], lat2 = t_location[0] )
        self.key = self.d + self.h
        self.p = -1
    
    def __le__(self, node):
        return self.key < node.key

    def __gt__(self, node):
        return self.key > node.key
    
    def __eq__(self, node):
        return self.key == node.key

def find_node(id,nodes):
    for u,node in enumerate(nodes):
        if node.id == id:
            return u

def find_path(s_id,t_index,nodes):
    path = []
    path.append(nodes[t_index].id)
    a = nodes[t_index].p
    while(a != s_id):
        path.append(a)
        a_index = find_node(a,nodes)
        a = nodes[a_index].p
    path.append(s_id)
    return path

def find_distance(s_id,t_index,nodes):
    distance = []
    distance.append(nodes[t_index].id)
    a = nodes[t_index].p
    while(a != s_id):
        distance.append(a)
        a_index = find_node(a,nodes)
        a = nodes[a_index].p
    distance.append(s_id)
    return distance



def a_star(start,destination):
    """
    start and destination should be the string form of s and t's id
    """
    nodes = []
    hp = heapdict.heapdict()
    s = Node(id = start,       location = nodes_dic[start],       t_location = nodes_dic[destination], neighbors = get_neighbors(start))
    s.d = 0
    s.key = 0 + s.h
    t = Node(id = destination, location = nodes_dic[destination], t_location = nodes_dic[destination], neighbors = get_neighbors(destination))
    nodes.append(s)
    nodes.append(t)
    hp[destination] = t.key
    hp[start] = s.key
    for node in nodes_dic:
        if node == s.id or node == t.id:
            continue
        else:
            try:
                node_c = Node(id = node, location = nodes_dic[node], t_location = nodes_dic[destination], neighbors = get_neighbors(node))
            except:
                node_c = Node(id = node, location = nodes_dic[node], t_location = nodes_dic[destination], neighbors = [])
            hp[node] = node_c.key
            nodes.append(node_c) 
    while len(hp):
        u = hp.popitem()
        u_index = find_node(u[0],nodes)
        if u[0] == t.id:  
            break
        for v in nodes[u_index].neighbors:
            v_index = find_node(v,nodes)
            Dv = nodes[u_index].d + distance(lon1=nodes[u_index].location[1],lat1=nodes[u_index].location[0],lon2=nodes[v_index].location[1],lat2=nodes[v_index].location[0])
            if Dv < nodes[v_index].d:
                nodes[v_index].d = Dv
                nodes[v_index].p = u[0]
                nodes[v_index].key = Dv + nodes[v_index].h
                try:
                    hp[nodes[v_index].id] = Dv + nodes[v_index].h
                except:
                    continue
    
    path = find_path(s_id = s.id, t_index = find_node(t.id,nodes), nodes = nodes)
    return path[::-1],t.d
        
        