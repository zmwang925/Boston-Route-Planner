
import json
from geopy.distance import geodesic 

inf = float("inf")

class Location:
    def __init__(self, id, lat=0, lon=0, adj = {}):
        self.id = id
        self.lat = float(lat)
        self.lon = float(lon)
        self.adj = adj

    def __str__(self):
        return 'id:' + str(self.id) + ', (lat: ' + str(self.lat) + ' lon: ' + str(self.lon)+'),\nadj:' + str(self.adj)

def Extract(locations, points):
    with open('new_src_des.json', 'r') as f:
        data = json.load(f)
        count = 0
        for key, value in data.items():
            location = Location(key)
            adj_dis = {}
            lat, lon = value['location'][0], value['location'][1]
            adj_points = list(value.keys())[1:]
            location.lat, location.lon = lat, lon

            for adj in adj_points:
                adj_dis[adj] = geodesic((value[adj][0], value[adj][1]), (lat, lon)).km
            location.adj = adj_dis
            locations.append(location)
            points[location.id] = count
            count += 1
    return locations,points

def Bellman_Ford_queue(src, locations, points, dis_from_src):
    ## Initialize
    inqueue = {}
    pred = {}
    Q = [src]
    for location in locations:
        if(location.id == src):
            dis_from_src[location.id] = 0
            inqueue[location.id] = True  
        else:
            dis_from_src[location.id] = inf
            inqueue[location.id] = False 
        pred[location.id] = None

    while(len(Q)):
        u = Q.pop(0)
        inqueue[u] = False
        for node in locations[points[u]].adj:
            weight = locations[points[u]].adj[node]
            if(node in dis_from_src):
                if(dis_from_src[node] > dis_from_src[u] + weight):
                    dis_from_src[node] = dis_from_src[u] + weight
                    pred[node] = u
                    if(inqueue[node] == False):
                        Q.append(node)
                        inqueue[node] = True
    return dis_from_src, pred

def route(src, des, pred):
    r = [des]
    node = des
    while(node != src):
        r.append(pred[node])
        node = pred[node]
    r.reverse()
    return r
