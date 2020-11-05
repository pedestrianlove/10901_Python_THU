from utils import underline

# function area
def factorial (n):
	summation = 1
	while (n >= 1):
		summation *= n
		n -= 1
	return summation
	
def isPrime (n):
	if ((factorial (n - 1) - 1) % n == 0):
		return True
	return False


# driver code

## input
num = eval (input ("Enter an integer greater than 1: " + underline.start))
print (underline.end, end='')

## process && output
print (num, end='')
if (isPrime (num)):
	print (" is a prime number.")
else:
	print (" is not a prime number.")
