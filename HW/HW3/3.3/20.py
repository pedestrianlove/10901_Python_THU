# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# set variables
rate = 1.011
population = 7

# process
years = 0
while (population < 8) :
	population *= rate
	years += 1

# output
print ("World population will be 8 billion in the year {:d}.".format (2011 + years))
	
	
	
