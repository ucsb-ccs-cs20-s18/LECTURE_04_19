import json

with open('slavery.json') as json_data:
    d = json.load(json_data)
    print(d)
