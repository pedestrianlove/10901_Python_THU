# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# set variables
rate = 1 - .00012
amount = 1

# process
years = 0
while (amount > 0.5) :
	amount *= rate
	years += 1

# output
print ("Carbon-14 has a half-life of {:d} years.".format (years))	
	
	
