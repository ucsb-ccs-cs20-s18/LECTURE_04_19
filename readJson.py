import json

# This code loads data from data_in.json
# into a Python dictionary called d

with open('data_in.json') as json_data:
    d = json.load(json_data)

d["four"]="quatro"
d["five"]="cinco"

with open('data_out.json', 'w') as outfile:
    json.dump(d, outfile)
