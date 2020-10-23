# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# set variables
rate = .85
car = 20000

# process && output
for i in range (4):
	car *= rate
	print (str (i+1), end='\t')
	print ("${:,.2f}".format (car))
