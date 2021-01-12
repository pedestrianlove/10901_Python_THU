import math

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
number = []
size = eval ( input ("How many numbers do you want to enter? " + underline.start))
print (underline.end, end='')

for i in range (size):
	number.append (eval ( input ("Enter a number: " + underline.start)))
	print (underline.end, end='')

# process
number.sort ()
if size % 2 == 0 :
	median = ( number [int (size / 2) - 1] + number [int (size / 2)] ) / 2 
else :
	median = number [ int ((size + 1) / 2) - 1 ]



# output
print ("Median: ", end='')
print ("{:.1f}".format (median))

	
	
	
