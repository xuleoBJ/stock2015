import json
filePathJson = "E:\\stock2015\\webScrapy\\喜马拉雅json\\index_tracks3.json"
with open(filePathJson, 'r') as f:  
    data = json.load(f) 
print(data["html"])
# print(data["title"])
