# Fibonacci Sequence
def Fibonacci (n):
	if n in [0, 1]:
		return n
	return Fibonacci (n - 1) + Fibonacci (n - 2)


# Driver code
n = int (input ("Enter a positive integer: "))
print ("Fibonacci number: {:d}".format (Fibonacci (n)))
