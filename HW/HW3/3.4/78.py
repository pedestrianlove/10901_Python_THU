def isValid (number) :
	if (str (number*4) == str (number)[::-1]):
		return True
	else:
		return False

def output (number) :
	print ("Since 4 times {:d} is {:d}, the special number is {:d}.".format (number, number*4, number))


for i in range (9999) :
	if (isValid (i+1)):
		output (i+1)

