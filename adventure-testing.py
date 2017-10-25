import random
import csv
import json
import textwrap


with open('rooms.json') as room_file:
    rooms = json.load(room_file)


with open('help.json') as help_file:
    help = json.load(help_file)
# Takes a room ID and column name from the rooms.csv file and returns the requested field!


class Player(object):
    def __init__(self, player_name, cur_room, inventory):
        self.player_name = player_name
        self.cur_room = cur_room
        self.inventory = inventory


# If provided with a room id and room quality, outputs value. formatting = rfield("0001", "short_desc").
def rfield(rid, rval):
    for i in rooms["rooms"]:
        if i == rid:
            return rooms["rooms"][rid][rval]


# Calls entire room record for the room id provided.
def rrecord(rid):
    for i in rooms["rooms"]:
        if i == rid:
            return rooms["rooms"][i]


def start_game():
    """Entering loop to allow for all the player commands"""
    # name = input("Who are you? (This is case sensitive) ")
    p = Player('Bob_Test', rfield("0001", "rid"), {})
    print("Hello " + str(p.player_name) + "!")
    print(textwrap.fill(rfield(p.cur_room, "short_desc"), 80))
    while True:
        action = ""
        print()
        action = input().lower().rstrip()
        if action.startswith('help'):
            if len(text) == 1:
                print(textwrap.fill(help["general"]))
            else:
                text = action.split(" ")
                try:
                    print(textwrap.fill(help[text[1]]))
                except KeyError:
                    print("No help record found for " + text[1])
        elif action.startswith('go') or action.startswith('enter'):
            text = action.split(" ")
            try:
                p.cur_room = rooms["rooms"][p.cur_room]["exits"][text[1]]
                print(textwrap.fill(rfield(p.cur_room, "short_desc")))
                continue
            except KeyError:
                print("I would if I could.  Maybe choose a direct with a way through.")
            continue
        elif action.startswith('look'):
            text = action.split(" ")
            if len(text) == 1:
                print(textwrap.fill(rfield(p.cur_room, "full_desc")))
                continue
            else:
                try:
                    print(textwrap.fill(rooms["rooms"][rooms["rooms"][p.cur_room]["exits"][text[1]]]["look_desc"]))
                    continue
                except KeyError:
                    print("Looks like a wall, ya' derp. Choose something else to look at.")
                    continue
            continue
        elif action.startswith('quit'):
            print("Game over man!")
            break
        else:
            print("I'm sorry, I don't understand that command.")

start_game()