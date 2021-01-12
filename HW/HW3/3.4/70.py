# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# open file
fp = open ("70.input", "r")

counter = 0
for ball in iter (fp):
	counter += 1
	if ('R' in ball and 'e' in ball and 'd' in ball):
		break

# close file
fp.close ()


# output
print ("The red ball was first drawn in turn {:d}.".format (counter))	
	
	
