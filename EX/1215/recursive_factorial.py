def factorial (n):
	if n == 0:
		return 1
	return n * factorial (n - 1)

# driver code
num = eval (input ("Please input a number to compute factorial: "))
print (factorial (num))
