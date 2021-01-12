# 5. Alphabetical Order
def isTripleConsecutive (word):
	for i in range (len (word)):
		if i <= (len (word) - 3) and ord (word[i]) + 1 == ord (word[i+1]) and ord (word[i+1]) + 1 == ord (word[i+2]):
			return True
	return False






# driver code
word = input ("Enter a word: ").strip ()
if isTripleConsecutive (word):
	print (word + " contains three successive letters in consecutive alphabetical order.")
else:
	print (word + " does not contain three successive letters in consecutive alphabetical order.")
