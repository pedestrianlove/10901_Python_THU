# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# function area
def isVowel (char) :
	return char.lower () in 'aeiou'






# input
word = input ("Enter word to translate: " + underline.start)
print (underline.end, end='')


# output
print ("The word in Pig Latin is ", end='')
if (isVowel (word[0])) :
	print (word + "way.")
else :
	counter = 0
	while (not isVowel (word[counter])):
		counter += 1;
	print (word[counter : ] + word[ : counter] + "ay.")
			
	
	
