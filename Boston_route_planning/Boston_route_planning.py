
import bellman_ford as bf
import dijkstra as dj
import a_star as astar

from Map_data import src_des_dic,way_node_dic
from geopy.distance import geodesic

inf = float("inf")

## Using get_coordinate to get the node closest to target node
def get_coordinate(psrc, nodes):
    dis = inf
    lat, lon = psrc[0], psrc[1]
    for key, value in nodes.items():
        dis_psrc = geodesic((value[0], value[1]), (lat, lon)).km
        if(dis_psrc < dis):
            dis = dis_psrc
            node = key
            coordinate = (value[0], value[1])
    return node, coordinate

## Bellman_Ford
def bellman_ford(src_id, des_id):
	locations = []
	points = {}
	dis_from_src = {}
	pred = {}
	node_pos_bf = []

	locations, points = bf.Extract(locations, points)

	dis_from_src, pred = bf.Bellman_Ford_queue(src_id, locations, points, dis_from_src)
	route_bf = bf.route(src_id, des_id, pred)
	dis_bf = dis_from_src[des_id]
	for node in route_bf:
		node_pos_bf.append(list(way_node_dic[node]))

	return node_pos_bf, route_bf, dis_bf

## Dijkstra
def dijkstra(src_pos, des_pos):
	graph = {}
	visited = []

	for key,value in src_des_dic.items():
		graph[key] = {}
		visited.append(key)
		lat1,lon1 = value["location"][0],value["location"][1]
		del value["location"]
		for k,v in value.items():
			lat2,lon2 = v[0],v[1]
			distance = geodesic((lat1, lon1), (lat2, lon2)).km
			graph[key][k] = distance

	for key in way_node_dic.keys():
		if key not in visited:
			graph[key] = {}

	src_flag, des_flag = False, False
	src, des = None, None

	for k,v in way_node_dic.items():
		if src_flag == False and v == src_pos:
			src = k
			src_flag = True
		if des_flag == False and v == des_pos:
			des = k
			des_flag = True
		if src_flag and des_flag:
			break 

	costs = {}
	parents = {}
	node_pos_dj = []
	dj.initialize_node_distance(way_node_dic,src,graph,costs)
	dj.initialize_node_parents(way_node_dic,src,graph,parents)

	dj.dijkstra(costs,parents,src,graph,des)
	route_dj = dj.find_shortest_path(parents,src,des)

	dis_dj = 0
	for i in range(len(route_dj)-1):
		dis_dj += graph[route_dj[i]][route_dj[i+1]]

	for node in route_dj:
		node_pos_dj.append(list(way_node_dic[node]))

	return node_pos_dj, route_dj, dis_dj

## A_Star
def a_star(src_id, des_id):
	node_pos_astar = []
	route_astar, dis_astar = astar.a_star(src_id, des_id)
	
	for node in route_astar:
		node_pos_astar.append(list(way_node_dic[node]))

	return node_pos_astar, route_astar, dis_astar


def route_plan(src_location,des_location,algorithm_choose):
    
## The src_location and des_location is transformed into some points on the graph
## to obtain the parameters needed by the three path planning algorithms
    src_id, src_pos = get_coordinate(src_location, way_node_dic)
    des_id, des_pos = get_coordinate(des_location, way_node_dic)

## Choose which algorithm to use
    if algorithm_choose == 'B':
        route_node_pos, route, src_des_dis = bellman_ford(src_id, des_id)
    elif algorithm_choose == 'D':
        route_node_pos, route, src_des_dis = dijkstra(src_pos, des_pos)
    elif algorithm_choose == 'A':
        route_node_pos, route, src_des_dis = a_star(src_id, des_id)

## Returns the longitude and latitude coordinates, ID and distance of the point on the path
    return route_node_pos, route, src_des_dis


if __name__ == '__main__':
    #Assumed coordinates
		psrc = (42.37052, -71.07553)
		pdes = (42.36570, -71.0767)
		route_node_pos, route, src_des_dis = route_plan(psrc,pdes,"B")
		print(route_node_pos)

