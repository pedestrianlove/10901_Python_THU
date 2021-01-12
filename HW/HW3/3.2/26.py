# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
bagel = eval ( input ("Enter number of bagels: " + underline.start))
print (underline.end, end='')


# output
print ("Cost is ", end='')
if (bagel < 6) :
	print ("${:.2f}.".format (bagel * 0.75))
else :
	print ("${:.2f}.".format (bagel * 0.60))

	
	
	
