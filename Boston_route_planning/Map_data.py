import json
import xml.dom.minidom



dom = xml.dom.minidom.parse('BostonMap.osm')
root = dom.documentElement
nodelist = root.getElementsByTagName('node')
waylist = root.getElementsByTagName('way')

node_dic = {}
node_dic2={}   # temporarily store the node information

way_dic = {}  # store all way 
way_node_dic = {}
src_des_dic = {}
#统计记录所有node
for node in nodelist:
    node_id = node.getAttribute('id')
    node_lat = float(node.getAttribute('lat'))
    node_lon = float(node.getAttribute('lon'))
    node_dic[node_id] = (node_lat, node_lon)


#得到路node
for way in waylist:
    taglist = way.getElementsByTagName('tag')
    way_id = way.getAttribute('id')
    road_flag = False
    oneway_flag = False
    for tag in taglist:
        if tag.getAttribute('k') == 'highway' and tag.getAttribute('v') != 'cycleway' and tag.getAttribute('v')!= 'footway':
            road_flag = True
            break
    for tag in taglist:
        if tag.getAttribute('k') == 'oneway':
            if tag.getAttribute('v') == 'yes':
                oneway_flag = True
                break
    if  road_flag:
        ndlist = way.getElementsByTagName('nd')
        node_dic2 = {}
        id_record = []
        for nd in ndlist:
            nd_id = nd.getAttribute('ref')
            node_lat = node_dic[nd_id][0]
            node_lon = node_dic[nd_id][1]
            node_dic2[nd_id] = (node_lat, node_lon)
            way_node_dic[nd_id] = (node_lat,node_lon)
            id_record.append(nd_id)
        way_dic[way_id] = node_dic2
        for i in range(len(node_dic2)-1):
            if id_record[i] not in src_des_dic:
                src_des_dic[id_record[i]] = {"location":node_dic[id_record[i]]}
            if id_record[i+1] not in src_des_dic[id_record[i]]:
                src_des_dic[id_record[i]][id_record[i+1]] = node_dic[id_record[i+1]]

            if not oneway_flag:
                if id_record[i+1] not in src_des_dic:
                    src_des_dic[id_record[i+1]] = {"location":node_dic[id_record[i+1]]}
                if id_record[i] not in src_des_dic[id_record[i+1]]:
                    src_des_dic[id_record[i+1]][id_record[i]] = node_dic[id_record[i]]

with open('new_way_node.json', 'w') as fout:
    json.dump(way_node_dic, fout)
with open('all_node.json', 'w') as fout: 
    json.dump(node_dic, fout)
with open('way_dic.json', 'w') as fout: 
    json.dump(way_dic, fout, indent = 1)
with open('new_src_des.json', 'w') as fout:
    json.dump(src_des_dic, fout,indent=1)