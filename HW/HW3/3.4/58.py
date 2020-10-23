# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
word = input ("Enter a word: " + underline.start)
print (underline.end, end='')



# process && output
print (word.upper (), end=' ')
if ('a' in word) and ('e' in word) and ('i' in word) and ('o' in word) and ('u' in word):
	print ("is a vowel word.")
else :
	print ("is not a vowel word.")



	
	
	
