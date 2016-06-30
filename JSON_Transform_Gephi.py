import json
from pprint import pprint
with open('/Users/qingping/Documents/Github/Network.json') as data_file:
    data = json.load(data_file)

f = open('/Users/qingping/Documents/Github/Network_Gephi.gdf','w')
f.write("nodedef>name VARCHAR,label VARCHAR\n")

for node in data["nodes"]:
    f.write(node["name"]+","+node["name"]+"\n")

f.write("edgedef>node1 VARCHAR,node2 VARCHAR\n")

for link in data["links"]:
    f.write(link["source"] + "," + link["target"] + "\n")


f.close()
#print(relations)
#pprint(data["nodes"])