# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# set variables
rate = 1.0025
deposit = 0

# process
months = 0
while (deposit <= 3000) :
	deposit *= rate
	deposit += 100
	months += 1

# output
print ("Annuity will be worth more than $3000 after {:d} months.".format (months))	
	
	
