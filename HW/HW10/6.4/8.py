# Sequence Of Numbers
def displaySequenceOfNumbers (m, n):
	if m <= n:
		print (m)
		displaySequenceOfNumbers (m + 1, n)


# Driver code
m = int (input ("Please enter a number as the start of sequence: "))
n = int (input ("Please enter a number as the end of sequence: "))
displaySequenceOfNumbers (m, n)
