# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
startingWord = input ("Starting word: ")

# process
counter = 0;
crossedOutLetters = ""
remainingLetters = ""
for char in startingWord:
	if (counter % 2 == 0) :
		crossedOutLetters = crossedOutLetters + char + " "
	else:
	 	remainingLetters = remainingLetters + char + " "
	counter += 1

# output
print ("Crossed out letters: ", end='')
print (crossedOutLetters)
print ("Remaining letters: ", end='')
print (remainingLetters)

	
	
	
