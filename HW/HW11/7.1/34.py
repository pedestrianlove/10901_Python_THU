from pCard import PlayingCard
import random

# function area
def card_count (card):
	suits = ["spades", "hearts", "diamonds", "clubs"]
	return suits.index (card.getSuit ())


# driver code
card_stonk = []

## generate card_stack
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', "10", "jack", "queen", "king", "ace"]
suits = ["spades", "hearts", "clubs", "diamonds"]
for rank in ranks:
	for suit in suits:
		card = PlayingCard ()
		card.setRank (rank)
		card.setSuit (suit)
		card_stonk.append (card)

## sample the card stack
sample = random.sample (card_stonk, 13)

## sort the sample
sample.sort (key = card_count)

## output the sample
for card in sample:
	print (card)
