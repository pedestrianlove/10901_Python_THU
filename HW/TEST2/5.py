# permutations


def perm (word, pre = ''):
	for i in range (len (word)):
		if i == 0:
			print (pre, end ='')
		print (word[i], end = ' ')
		pre = pre + word[i]
		word.remove (pre[-1])
		perm (word, i == 0, pre)
		word.insert (i, pre[-1])
	print (' ', end ='')




word = input ("Enter a word: ").strip ()
word_list = list (word)
perm (word_list)
print ()
