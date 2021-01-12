from pCard import PlayingCard

card = PlayingCard ()

while (card.getSuit () != "diamonds"):
	card.selectAtRandom ()

print (card)
