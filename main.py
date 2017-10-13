"""initialize the connection and wait for a message directed at it"""
from irc import *
from decision import *
import os
import random
 
channel = "#bitswebteam"
server = "irc.freenode.net"
nickname = "EisBot"
 
irc = IRC()
irc.connect(server, channel, nickname)
 
 
while 1:
    text = irc.get_text()
    print text
 
    if "PRIVMSG" in text and channel in text and "@choose" in text:
    	irc.send(channel, decision.decide(text))
    elif "PRIVMSG" in text and channel in text and "@adventure" in text:
    	irc.send(channel, "The adventure begins!..")
    	adventure.start()
