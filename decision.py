import random
import re

def decide(desc):
	l = desc.split('?', '@choose')
	item = ''
	for i in l:
		item += i
	lis = item.split(" or ")
	ran = random.randint(0,(len(lis)-1))
	return "I chooose... " + lis[ran] + "!!"