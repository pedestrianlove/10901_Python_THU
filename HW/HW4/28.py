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
	else :
		print ("Input error, please input again.")	

def fact (number) :
	count = 1
	while (number >= 1):
		count *= number
		number -= 1
	return count


# Flow control && Output
number = getN () 
print ("{:d}! is {:d}".format (number, fact (number)))
	
	
