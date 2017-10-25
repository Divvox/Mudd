import json
import pprint


with open('rooms.json') as room_file:
    rooms = json.load(room_file)
#    print(json.dumps(rooms, indent=4))
    for i in rooms["rooms"]:
        print(rooms["rooms"][i]["short_desc"])

