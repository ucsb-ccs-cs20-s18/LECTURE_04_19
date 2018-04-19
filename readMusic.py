import json


# This code loads data from music.json
# into a Python object, which could be a dictionary
# or it could be a list.  In this case, it's a list.

with open('music.json') as json_data:
    music = json.load(json_data)

shorterList = music[0:3]

# Writes a shorter list to music3.json

with open('music3.json', 'w') as outfile:
    json.dump(shorterList, outfile)
