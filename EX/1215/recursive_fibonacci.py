def fibonacci (n):
	if n in [0, 1]:
		return n
	return fibonacci (n - 1) + fibonacci (n - 2)


# driver code
num = eval (input ("Please input a number to compute fibonacci sequence's nth term: "))
print (fibonacci (num))

		
