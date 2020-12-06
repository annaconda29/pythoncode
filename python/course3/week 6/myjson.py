import json
data = '''{
    "Name" : "Annu", 
    "sister" : {"name" : "Vaishu",
    "type" : "Naughty"}
    }'''
info = json.loads(data)
print(type(info))
print("Name: ", info["Name"])
print("Sister Type: ", info["sister"]["type"])