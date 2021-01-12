import pickle
import os

def main ():
	fileName = os.path.join ("..", "CH5", "UNdict.dat")
	nations = getDictionary (fileName)
	continent = input ("Enter the name of a continent other than Antarctica: ")
	continentDict = constructContinentNations (nations, continent)
	displaySortedResults (continentDict)

def getDictionary (fileName):
	infile = open (fileName, 'rb')	# Read binary
	countries = pickle.load (infile)
	infile.close ()
	return countries

def constructContinentNations (nations, continent):
	continentDict = {}
	for nation in nations:
		if nations[nation]["cont"] == continent:
			continentDict[nation] = nations[nation]
	return continentDict

def displaySortedResults (dictionaryName):
	continentList = sorted (dictionaryName.items (), key = lambda x:x[1]["popl"], reverse = True)
	for k in continentList:
		print ("   {0:s}: {1:,.2f}".format (k[0], k[1]["popl"]))

# driver code
main ()
