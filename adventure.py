from irc import *
import random

class Player(object):	
	def __init__(self, player_name, cur_room, inventory):
		self.player_name = player_name
		self.cur_room = cur_room
		self.inventory = inventory
	

"""Sets up room object for use in formatting each room's data, to be stored in a DB.  Need to figure out how to have this equal the room the player is in...
		Maybe if I store room ID in the player object, I can keep data from overlapping and just directly reference a player's info so multiple people can play"""


"""Entering loop to allow for all the player commands"""
def start_game():
	pName = raw_input("Who are you? (This is case sensitive) ").strip
	starting_room = 1
	p = Player(pName, 1, inventory)
	
#  Section for game save code, commented out so I can test the game before I figure the damn thing out
#	try:
#		with open(player_name + ".txt", 'r') as file:
#			file.read(PULL DATA INTO IN-GAME OBJECTS FROM PLAYER AND GAME-STATE INFO)
#	except FileNotFoundError:
#		with open(player_name + ".txt", 'w') as file:
#			file.write(SET THE STARTER PLAYER OBJECT W/ STARTING ROOM DATA, FOLLOWED BY THE BLANK GAME-STATE OBJECT)
		
	while True:
		print p.cur_room
		action = ""
		action = input("What do you do? ").lower().rstrip()
		if action.beginsWith('go'):
			text = action.split(" ")
			if text[1] == "north" or text[1] == "south" or text[1] == "east" or text[1] == "west" or text[1] == "up" or text[1] == "down":
				if player.cur_room[text[1]] == 0:
					print "Ouch!  That's a wall!"
					continue
				else: 
					"""Call and set the room dictionary to match the ID listed in the appropriate direction field"""
					print player.cur_room[short_desc]
					continue
			else:
				print "I don't understand that direction!"
				continue
		elif action.beginsWith('look'):
			text = action.split(" ")
			if text[1] == "north" or text[1] == "south" or text[1] == "east" or text[1] == "west" or text[1] == "up" or text[1] == "down":
				if player.cur_room[text[1]] == 0:
					print "You see a wall!  Try looking in a different direction."
					continue
				elif text[1] == Null:
					print player.cur_room.full_desc
				else: 
					print c.execute(SELECT look_desc FROM RoomTable WHERE ID = player.cur_room[text[1]]) """I think it works something like this, but still need to import 
							SQLite and dec what DB c is calling to...  Can I put python variables into SQL queries like this?"""
					continue
			else:
				print "I don't understand that direction!"
				continue
		elif action == "quit" or action == "exit"
			"""Do some kind of game save function, hell if i know atm.  It's looking like I can just save the player class record, and the user can enter their player name to 
					continue the game (or it references their IRC account)"""
			print "Game saved, later tater!"
			break
		elif action == "get " + *:
			