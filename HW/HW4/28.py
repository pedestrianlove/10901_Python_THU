# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
def getN () :
	N = eval ( input ("Enter a positive integer: " + underline.start))
	print (underline.end, end='')
	if (N >= 0):
		return int (N)

def fact (number) :
	if (number <= 1) :
		return 1
	else :
	 	return number * fact (number - 1)


# Flow control && Output
number = getN () 
print ("{:d}! is {:d}".format (number, fact (number)))
	
	
