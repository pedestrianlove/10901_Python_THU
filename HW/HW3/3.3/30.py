# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# set variables
rate = .079
coffee = 212
ambient = 70

# process
minutes = 0
while ( coffee >= 150 ) :
	coffee -= rate * (coffee - ambient)
	minutes += 1

# output
print ("The coffee will cool to below 150 degrees in {:d} minutes.".format (minutes))	
	
	
