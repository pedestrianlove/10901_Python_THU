# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# set variables
rate = 1.0025
deposit = 0

# process && output
print ("\t BALANCE AT")
print ("YEAR\t", end='')
print ("END OF YEAR")
months = 0
year = 2014
while (year <= 2018) :
	deposit *= rate
	deposit += 100
	months += 1
	if (months % 12 == 0):
		print (str (year), end='\t')
		print ("${:,.2f}".format (deposit))
		year += 1
