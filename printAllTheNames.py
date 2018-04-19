
import json

import pprint
import sec2MSS

with open('music3.json') as json_data:
    music = json.load(json_data)

# print all the names



for song in music:
    print("release name:",song["release"]["name"])
    print("song title:",song["song"]["title"])
    print("tempo:",song["song"]["tempo"]," bpm")
    print("terms:",song["artist"]["terms"])
    print("duration:",sec2MSS.sec2MSS(song["song"]["duration"]))
    print("artist:",song["artist"]["name"])

