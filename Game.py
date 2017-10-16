import csv
csv.register_dialect('piper', delimiter='|',
def go_room(roomID):
	fp = open("rooms.txt")
	for i in enumerate(fp):
		if i == beginsWith(roomID):
			cur_room = line.split('|')
			


while True:
	print cur_room
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
	elif action.beginsWith('quit') or action.beginsWith('exit'):
		"""Do some kind of game save function, hell if i know atm.  It's looking like I can just save the player class record, and the user can enter their player name to 
				continue the game (or it references their IRC account)"""
		print "Later tater!"
		break
	elif action.beginsWith('get'):