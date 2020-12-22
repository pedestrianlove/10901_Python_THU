import pickle

# load from file
infile = open ("DeckOfCardsList.dat", 'rb')
card_list = pickle.load(infile)
infile.close()

print (obj)
