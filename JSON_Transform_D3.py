import json
from pprint import pprint
with open('/Users/qingping/Documents/Github/Network.json') as data_file:
    data = json.load(data_file)

f = open('/Users/qingping/Documents/Github/Network_d3.json','w')

nodes = data["nodes"]
names = []
keep_names = []
for node in nodes:
    names.append(node["name"])
    keep_names.append(0)
print(names)

links = data["links"]
relations = [[0 for y in range(len(names))] for x in range(len(names))]
for link in links:
    i = names.index(link["source"])
    j = names.index(link["target"])
    relations[i][j] = 1


for i in range(len(names)):
    for j in range(len(names)):
        if relations[i][j] == relations[j][i] and relations[j][i] != 0:
            keep_names[i] = 1
            keep_names[j] = 1

f.write("{\"nodes\":[\n")
count=0;
for i in range(len(names)):
    if keep_names[i] == 1:
        keep_names[i]+=count
        count+=1
        if i!=(len(names)-1):
            f.write("{\"name\":\"" + names[i] + "\"},\n")
        else:
            f.write("{\"name\":\"" + names[i] + "\"}\n")


f.write("],\"links\":[\n")

for i in range(len(names)):
    for j in range(0,i):
        if relations[i][j]  != 0 and relations[j][i]  != 0:
            if i==(len(names)-1) and j==(len(names)-1):
                f.write("{\"source\":"+str(keep_names[i]-1)+",\"target\":"+str(keep_names[j]-1)+"}\n")
            else:
                f.write("{\"source\":" +str(keep_names[i]-1) + ",\"target\":" + str(keep_names[j]-1) + "},\n")

f.write("]\n}")
f.close()
#print(relations)
#pprint(data["nodes"])