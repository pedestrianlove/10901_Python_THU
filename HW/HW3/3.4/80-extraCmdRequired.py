# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# variables
counter = 0
try:
	while (True):
		counter += 1
		tmp = input ()
		if (counter == 4):
			break
except EOFError:
	pass


# output
print ("The {:d}th winner was ".format (counter) + tmp)
	
	
