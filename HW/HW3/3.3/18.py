# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
N = eval ( input ("Enter a positive integer (>1): " + underline.start))
print (underline.end, end='')

# output
print ("Prime factors are ", end='')
F = 2
while (N > 1) :
	if (N % F == 0):
		print (str (F), end=' ')
		N = N / F
	else:
		F += 1

print ()

	
	
	
