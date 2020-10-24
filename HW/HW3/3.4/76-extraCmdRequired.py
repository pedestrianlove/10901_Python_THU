# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# variables
states = []


# input
try:
	while (True):
		states.append ( input () )

except EOFError:
	pass

# process
states.sort ()


# output
for state in states:
	print (state)


	
	
