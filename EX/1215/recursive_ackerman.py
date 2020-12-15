def ackermann (m, n):
	if m == 0:
		return n + 1
	else:
		if n == 0:	
			return ackermann (m - 1, 1)
		else:
			return ackermann (m - 1, ackermann (m, n - 1))

# driver code
m = eval (input ("Please input 2 positive number to compute ackermann function terms: "))
n = eval (input ("Please input 2 positive number to compute ackermann function terms: "))
print (ackermann (m, n))

