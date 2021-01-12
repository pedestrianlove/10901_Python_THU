def isVowelWord (word) :
	word = word.lower ()
	for vowel in 'aeiou':
		if vowel not in word :
			return False
	return True

word = input ("Enter a word: ")
print (word, end='')
if isVowelWord (word) :
	print (" contains every vowel.")
else :
	print (" does not contain every vowel.")
