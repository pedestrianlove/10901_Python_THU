# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# file open
fp = open ("80.input", "r")

# input
counter = 0
for tmp in iter (fp) :
	counter += 1
	if (counter == 4):
		break

# file close
fp.close ()

# output
print ("The {:d}th winner was ".format (counter) + tmp)
	
	
