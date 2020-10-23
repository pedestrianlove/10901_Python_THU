# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# variables
deposit = 10000.0
lost = 0.84
gain = 1.18


# process
for i in range (6):
	deposit *= lost
for i in range (6):
	deposit *= gain

print ("The value of the stock at the end of the year was: ", end='')
print ("${:,.2f}".format (deposit))

	
	
	
