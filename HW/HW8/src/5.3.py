import os
import pickle
import operator

# 5.3 - 50
print ("5.3 - 50.")
topHitters = {"Gehrig": {"atBats": 8061, "hits": 2721}, "Ruth": {"atBats": 8399, "hits": 2873}, "Williams": {"atBats": 7706, "hits": 2654}}
## OUTPUT
maxi = -1
for man in topHitters:
	if maxi == 0:
		maxi = topHitters[man]['hits']
	elif maxi < topHitters[man]['hits']:
		maxi = topHitters[man]['hits']
print ("The most hits by one of the baseball players was", maxi)
print ()
print ()



# 5.3 - 52
print ("5.3 - 52.")
## INPUT
state = input ("Enter a state abbreviation: ")
fileName = os.path.join ("..", "data", "JusticesDict.dat")
infile = open (fileName, 'rb')
Justices = pickle.load (infile)
infile.close ()
## OUTPUT
for man in Justices:
	if Justices[man]['state'] == state:
		print (man + '\t' + str (Justices[man]['yrAppt']))
print ()
print ()



# 5.3 - 54
print ("5.3 - 54")
print ()
print ()



# 5.3 - 56
print ("5.3 - 56")
## INPUT
fileName = os.path.join ("..", "data", "Rosebowl.txt")
infile = open (fileName, 'r')
WINNER = []
for winner in iter (infile):
	if winner.strip () in WINNER:
		WINNER[WINNER.index (winner)][1] += 1
	else:
		WINNER.append ([winner.strip (), 1])
infile.close ()
WINNER.sort (key = lambda elem : elem[1], reverse = True)
## OUTPUT
print ("Teams with four or more Rose Bowl wins as of 2014:")
for winner in WINNER:
	if winner[1] >= 4:
		print (winner[0], ': ', winner[1])
print ()
print ()
