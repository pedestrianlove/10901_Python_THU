# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# variables
states = []

# open file
fp = open ("76.input", "r")

# input
for state in iter (fp) :
	states.append ( state )
# close file
fp.close ()


# process
states.sort ()


# output
for state in states:
	print (state)


	
	
