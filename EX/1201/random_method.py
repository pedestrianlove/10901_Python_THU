import random
import pickle
import os

fileName = os.path.join ("..", "CH6", "DeckOfCardsList.dat")
infile = open (fileName, 'rb')
deckOfCards = pickle.load (infile)
infile.close ()

pokerHand = random.sample (deckOfCards, 5)
print (pokerHand)

