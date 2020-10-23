# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# variables
counter = 0
try:
	while (True):
		counter += 1
		ball = input ()
		if ('R' in ball and 'e' in ball and 'd' in ball):
			break
except EOFError:
	pass

# output
print ("The red ball was first drawn in turn {:d}.".format (counter))	
	
	
