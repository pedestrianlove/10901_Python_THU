# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
year = eval ( input ("Enter a year: " + underline.start))
print (underline.end, end='')


# output
print ("{:d} ".format (year), end='')

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) :
	print ("is", end='')
else :
	print ("is not", end='')

print (" a leap year.")
	
	
	
