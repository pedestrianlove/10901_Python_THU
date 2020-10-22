# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
N = eval ( input ("Enter a number: " + underline.start))
print (underline.end, end='')

# output
F = 2
while (N > 1) :
	if (N % F == 0):
		print (F)
		N = N / F
	else:
		F += 1


	
	
	
