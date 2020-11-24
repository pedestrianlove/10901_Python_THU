def main ():
	texteseDict = createDictionary ("../CH5/Textese.txt")
	print ("Enter a simple sentence in lower case letters without")
	sentence = input ("any punctuation: ")
	translate (sentence, texteseDict)
	print ()

def createDictionary (fileName):
	infile = open (fileName, 'r')
	textList = [line.rstrip () for line in iter (infile)]
	infile.close ()
	return dict ([x.split (',') for x in textList])

def translate (sentence, texteseDict):
	words = sentence.split ()
	for word in words:
		print (texteseDict.get (word, word) + " ", end = '')

# driver code
main ()
