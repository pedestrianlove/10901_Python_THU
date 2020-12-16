# Mortgage
def Mortgage (p, pmt, r, n):
	if n == 0:
		return p
	return (1 + (r / 1200)) * Mortgage (p, pmt, r, n - 1) - pmt


# Driver code
p = float (input ("Enter the principal: "))
r = float (input ("Enter the annual rate of interest: "))
pmt = float (input ("Enter the monthly payment: "))
n = int (input ("Enter the number of monthly payment made: "))

print ("The amount still owed is ${:,.2f}.".format (Mortgage (p, pmt, r, n)))
