from irc import *
import random

class Player(object):
	"""This room bit will probably end up being blank, with it being populated with the default room for a new character and the obj saved with the current room data, all from the
			DB instead of trying to outline fields here..."""
	cur_room = {
			id = 0
			short_desc = "The player sees this when they enter the room."
			full_desc = "The player sees this when they use the look command."
			look_desc = "The player sees this when they look at the room from an adjacent room"
			north = 0
			ndoor = False
			nlock = False
			south = 0
			sdoor = False
			slock = False
			east = 0
			edoor = False
			elock = False
			west = 0
			wdoor = False
			wlock = False
			up = 0
			udoor = False
			ulock = False
			down = 0
			ddoor = False
			dlock = False
			r_inv = []
		}
	def __init__(self, player_name, cur_room, inventory):
		self.player_name = player_name
		
		self.inventory = {}
	
"""Sets up room object for use in formatting each room's data, to be stored in a DB.  Need to figure out how to have this equal the room the player is in...
		Maybe if I store room ID in the player object, I can keep data from overlapping and just directly reference a player's info so multiple people can play"""


"""Entering loop to allow for all the player commands"""
def start_game():
	while True:
		action = ""
		action = input("What do you do? ").lower().strip()
		if action == "go " + *:  """Is this right?  Might throw an error..."""
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
		elif action == "look " + *:
			text = action.split(" ")
			if text[1] == "north" or text[1] == "south" or text[1] == "east" or text[1] == "west" or text[1] == "up" or text[1] == "down":
				if player.cur_room[text[1]] == 0:
					print "You see a wall!  Try looking in a different direction!"
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
			