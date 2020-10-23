# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input && process

num = eval ( input ("Enter a number: " + underline.start))
print (underline.end, end='')
max_n = num

for i in range(2):
	tmp = eval ( input ("Enter a number: " + underline.start))
	print (underline.end, end='')
	if (tmp > max_n):
		max_n = tmp


# output
print ("Largest number: ", end='')
print ("{:.1f}".format (max_n))

	
	
	
