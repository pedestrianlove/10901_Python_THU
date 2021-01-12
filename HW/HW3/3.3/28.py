# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# set variables
rate = 1.003
deposit = eval (input ("Please input your deposit savings: " + underline.start))
print (underline.end, end='')

# process
months = 0
while (deposit >= 600 ) :
	deposit = deposit * rate - 600
	months += 1

# output
print ("Balance will be ${:,.2f} after {:d} months.".format (deposit ,months))	
	
	
