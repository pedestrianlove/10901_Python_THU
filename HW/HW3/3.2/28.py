# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
copy = eval ( input ("Enter number of copies: " + underline.start))
print (underline.end, end='')


# output
print ("Cost is ", end='')
if (copy < 100) :
	print ("${:.2f}.".format (copy * 0.05))
else :
	print ("${:.2f}.".format (5 + (copy-100) * 0.03))

	
	
	
