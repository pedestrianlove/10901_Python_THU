# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
first = eval ( input ("Enter cost of the first suit: " + underline.start))
print (underline.end, end='')
second = eval ( input ("Enter cost of the second suit: " + underline.start))
print (underline.end, end='')


# output
print ("Cost of the two suits is ", end='')
if (first <= second) :
	print ("${:.2f}".format (first * 0.5 + second))
else :
	print ("${:.2f}".format (second * 0.5 + first))

	
	
	
