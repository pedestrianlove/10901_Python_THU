# 6. ISBN

def isValid (ISBN):
	new_ISBN = []
	for char in ISBN:
		if char != '-':
			if (char == 'X'):
				new_ISBN.append (10)
			else:
				new_ISBN.append (int (char))

	summation = 0
	for i in range (1, len (new_ISBN) + 1):
		summation += (10 - i+1) * new_ISBN[i-1]
	if summation % 11 == 0:
		return True
	else:
		return False

ISBN = input ("Enter an ISBN: ").strip ()
if isValid (ISBN):
	print ("The number is valid.")
else:
	print ("The number is invalid.")

