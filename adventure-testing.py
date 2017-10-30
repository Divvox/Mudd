import random
import json
import textwrap


class Player(object):
    changes = {"rooms": {"0000": {"rid": "0000"}}, "doors": {"0000": "closed"}}

    def __init__(self, player_name, cur_room, inventory):
        self.player_name = player_name
        self.cur_room = cur_room
        self.inventory = inventory


# opening important files.  I need to look into pulling primary work out of the main file, so it is cleaner.
# Still trying to figure out how and what the hell __main__ == __something__ is all about...
with open('rooms.json') as room_file:
    rooms = json.load(room_file)


with open('Main_Reference.json') as ref_file:
    ref = json.load(ref_file)


with open('Items.json') as item_file:
    inv = json.load(item_file)


# If provided with a room id and room quality, outputs string.
def rfield(rid, rval):
    for i in rooms["rooms"]:
        if i == rid:
            return rooms["rooms"][rid][rval]


# Call and output item value.
def ifield(iid, ival):
    for i in inv:
        if i == iid:
            return inv[iid][ival]


# Calls entire room record for the room id provided.
def rrecord(rid):
    for i in rooms["rooms"]:
        if i == rid:
            return rooms["rooms"][i]


# Generate random error for a bad move attempt.
def move_error():
    r = str(random.randrange(1, 5))
    return ref["moveerrors"][r]


# generate random error for a bad look attempt.
def look_error():
    r = str(random.randrange(1, 4))
    return ref["lookerrors"][r]


# generate error for missing door open/close command.
def door_error(y):
    if y == "north" or y == "south" or y == "east" or y == "west" or y == "up" or y == "down":
        print("There is nothing to open to the " + y + ".")
    else:
        print("There is no " + y + " here.")


# Generates a list of available exits for the indicated room.
def exits(rid):
    ex = ""
    for i in rooms["rooms"][rid]["exitdesc"].values():
        ex = ex + "\n" + i
    return ex


# checks if a room field has had changes to it
def checkit(lib, rid, rfld, rdetail):
    try:
        if rid in lib:
            if rfld in lib[rid]:
                if rdetail in lib[rid][rfld]:
                    return "yes"
    except KeyError:
        return "no"


def room_ordered(r1, r2):
    if int(r1) < int(r2):
        return r1 + "," + r2
    else:
        return r2 + "," + r1


def door_exists(player, r1, r2):
    a = r1 + "," + r2
    b = r2 + "," + r1
    try:
        for i in player.changes["doors"]:
            if i == a or i == b:
                return player.changes["doors"][i]
        for x in ref["doors"]:
            if x == a or x == b:
                return ref["doors"][x]
            else:
                return "no"
    except KeyError:
        try:
            for x in ref["doors"]:
                if x == a or x == b:
                    return ref["doors"][x]
                else:
                    return "no"
        except KeyError:
            return "no"


# Starts the game!
def start_game():
    """Entering loop to allow for all the player commands"""
    # name = input("Who are you? (This is case sensitive) ")
    p = Player('Bob_Test', rfield("0001", "rid"), {})
    print("Hello " + str(p.player_name) + "! \n")
    print(textwrap.fill(rfield(p.cur_room, "short_desc"), 100))
    while True:
        print()
        action = input(">>>").lower().rstrip()
        text = action.split(" ")
        if text[0] == "help":
            if len(text) == 1:
                for i in ref["help"]:
                    print(textwrap.fill(ref["help"][i], 100) + "\n")
                    continue
            else:
                try:
                    print(textwrap.fill(ref["help"][text[1]], 100))
                except KeyError:
                    print("No help record found for " + text[1])
        elif action.startswith('exits'):
            try:
                print(textwrap.fill(exits(p.cur_room), 100))
            except KeyError:
                print("Error: exit descriptions not provided for this room, poke Sam in the side.")
        elif text[0] == "go" or text[0] == "enter":
            if len(text) == 1:
                if text[0] == "go":
                    print("Go where?")
                    continue
                else:
                    print("What should I enter?")
                    continue
            else:
                try:
                    if text[1] in rooms["rooms"][p.cur_room]["exits"]:
                        if door_exists(p, p.cur_room, rooms["rooms"][p.cur_room]["exits"][text[1]]) == "closed":
                            print("Ow, there's a door there...")
                            continue
                        else:
                            p.cur_room = rooms["rooms"][p.cur_room]["exits"][text[1]]
                            print(textwrap.fill(rfield(p.cur_room, "short_desc"), 100))
                            continue
                    else:
                        print(move_error())
                except KeyError:
                    print(move_error())
        elif text[0] == "look":
            if len(text) == 1:
                print(textwrap.fill(rfield(p.cur_room, "full_desc"), 100))
                continue
            else:
                try:
                    door = door_exists(p, p.cur_room, rooms["rooms"][p.cur_room]["exits"][text[1]])
                    if door == "closed":
                        print("There's a closed door there.")
                    else:
                        print(textwrap.fill(rooms["rooms"][rooms["rooms"][p.cur_room]["exits"][text[1]]]["look_desc"], 100))
                        continue
                except KeyError:
                    print(look_error())
                    continue
        elif text[0] == "open" or text[0] == "close":  # open/close an object
            try:
                if text[1] in rooms["rooms"][p.cur_room]["exits"]:
                    door = door_exists(p, p.cur_room, rooms["rooms"][p.cur_room]["exits"][text[1]])
                    cdoor = room_ordered(p.cur_room, rooms["rooms"][p.cur_room]["exits"][text[1]])
                    if door == "closed" and text[0] == "open":
                        p.changes["doors"][cdoor] = "open"
                        print("You open the door.")
                    elif door == "open" and text[0] == "close":
                        p.changes["doors"][cdoor] = "closed"
                        print("You close the door.")
                    elif door == "open" and text[0] == "open":
                        print("That door is already open.")
                    elif door == "closed" and text[0] == "closed":
                        print("that door is already closed.")
                    else:
                        print(door_error(text[1]))
                else:
                    print("derp")
            except KeyError:
                print(door_error(text[1]))
        elif text[0] == "quit":
            print("Game over man!")
            break
        elif text[0] == "room_changes":
            print(p.changes)
        else:
            print("I'm sorry, I don't understand that command.")


start_game()
