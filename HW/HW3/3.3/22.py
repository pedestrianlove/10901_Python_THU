# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# set variables
rate = 1.025
cpi = 1

# process
years = 0
while (cpi < 2) :
	cpi *= rate
	years += 1

# output
print ("Consumer prices will double in {:d} years.".format (years))	
	
	
