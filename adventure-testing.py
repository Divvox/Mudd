import random
import csv

roomfile = open('rooms.csv', "r")
roomreader = csv.reader(roomfile, delimiter='|')

# Takes a room ID and column name from the rooms.csv file and returns the requested field!


class Player(object):
    def __init__(self, player_name, cur_room, inventory):
        self.player_name = player_name
        self.cur_room = cur_room
        self.inventory = inventory


def rfield(roomid, column_name):
    rownum = 0
    for row in roomreader:
        if rownum == 0:
            header = row
        else:
            if row[0] == roomid:
                desrow = dict(zip(header, row))
                return desrow[column_name]
        rownum += 1


print(rfield('0001', 'short_desc'))


def crrec(roomid):
    rownum = 0
    for row in roomreader:
        if rownum == 0:
            header = row
        else:
            if row[0] == roomid:
                desrow = dict(zip(header, row))
                return desrow
        rownum += 1


def start_game():
    """Entering loop to allow for all the player commands"""
    # name = input("Who are you? (This is case sensitive) ")
    p = Player('Bob_Test', crrec('0001'), {})
    print("Hello " + str(p.player_name) + "!")
    print(p.cur_room['short_desc'])
    while True:
        action = ""
        print()
        action = input("What do you do? ").lower().rstrip()
        if action.startswith('go'):
            text = action.split(" ")
            if text[1] == "north" or text[1] == "south" or text[1] == "east" or text[1] == "west" or text[1] == "up" or text[1] == "down":
                if p.cur_room[text[1]] == 0:
                    print("Ouch!  That's a wall!")
                    continue
                else:
                    p.cur_room = crrec(p.cur_room[text[1]])
                    print(p.cur_room[short_desc])
                    continue
            else:
                print("I don't understand that direction!")
                continue
            continue
        elif action.startswith('look'):
            text = action.split(" ")
            if len(text) == 1:
                text.append('cur')
            if text[1] == "north" or text[1] == "south" or text[1] == "east" or text[1] == "west" or text[1] == "up" or text[1] == "down":
                if p.cur_room[text[1]] == 0:
                    print("You see a wall!  Try looking in a different direction.")
                    continue
                elif text[1] == 'cur':
                    print(p.cur_room[full_desc])
                    continue
                else:
                    print(rfield(p.cur_room[text[1], look_desc]))
                    continue
            continue


start_game()