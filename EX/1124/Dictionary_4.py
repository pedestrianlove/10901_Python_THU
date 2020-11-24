def main ():
	WordList = formWordList ("../CH5/Gettysburg.txt")
	freq = createFreqDict (WordList)
	displayWordCount (WordList, freq)
	displayMostCommonWords (freq)

def formWordList (fileName):
	infile = open (fileName)
	orig = infile.readline ().strip ().lower ()
	line = ''
	for ch in orig:
		if 'a' <= ch <= 'z' or ch == ' ':
			line += ch
	return line.split ()
	
def createFreqDict (listOfWords):
	freq = {}
	for word in listOfWords:
		freq[word] = 0
	for word in listOfWords:
		freq[word] += 1
	return freq

def displayWordCount (listOfWords, freq):
	print ("The Gettysburg Address contains", len (listOfWords), "words.")
	print ("The Gettysburg Address contains", len (freq), "different words.")
	print ()

def displayMostCommonWords (freq):
	print ("The most common words and their frequencies are:")
	listOfMostCommonWords = []
	for word in freq.keys ():
		if freq[word] >= 6:
			listOfMostCommonWords.append ((word, freq[word]))
	listOfMostCommonWords.sort (key = lambda x : x[1], reverse = True)
	for item in listOfMostCommonWords:
		 print ("   ", item[0] + ':', item[1])


# driver code 
main ()

