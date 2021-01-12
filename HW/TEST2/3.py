import pickle
import random

def card_type (card):
	typeList = [0, 0]
	if card[1] == '♠':
		typeList[0] = 1
	elif card[1] == '♥':
		typeList[0] = 2
	elif card[1] == '♣':
		typeList[0] = 3
	elif card[1] == '♦':
		typeList[0] = 4
	
	if card[0] == 'A':
		typeList[1] = 1
	elif card[0] == 'J':
		typeList[1] = 11
	elif card[0] == 'Q':
		typeList[1] = 12
	elif card[0] == 'K':
		typeList[1] = 13
	else:
		typeList[1] = int (card[0])
	return typeList



# load from file
infile = open ("DeckOfCardsList.dat", 'rb')
card_list = pickle.load(infile)
infile.close()

# random sample 5 card
list1 = random.sample (card_list, 13)
print (','.join (list1))
list1.sort (key = lambda x: card_type (x)[0])
kind_count = [0, 0, 0, 0]

for card in list1:
	kind = card_type (card)
	kind_count[kind[0]] += 1

for kinds in kind_count:
	print ("Number of ")
