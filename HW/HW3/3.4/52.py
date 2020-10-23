# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
Telefonnummer =  input ("Enter a telephone number: " + underline.start)
print (underline.end, end='')

# process && output
print ("Number without dashes is ", end='')
for char in Telefonnummer :
	if (char != '-'):
		print (char, end='')

print (".")

	
	
	
