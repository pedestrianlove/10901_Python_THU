import pickle
import os

def main ():
	fileName = os.path.join ("..", "CH5", "USpresStatesDict.dat")
	presDict = createDictFromBinaryFile (fileName)
	state = getState (presDict)
	displayOutput (state, presDict)

def createDictFromBinaryFile (fileName):
	infile = open (fileName, 'rb')
	dictionaryName = pickle.load (infile)
	infile.close ()
	return dictionaryName

def getState (dictName):
	state = input ("Enter the name of a state: ")
	if state in dictName.values ():
		return state
	else:
		return "There are no presidents from " + state + '.'

def displayOutput (state, dictName):
	if state.startswith ("There"):
		print (state)
	else:
		print ("Presidents from", state + ':')
		for pres in sorted (dictName):
			print (" " + pres[1] + " " + pres[0])

# driver code
main ()
