# pascal triangle

def pascal (row, col):
	if col == 0 or (col == row) or row == 0:
		return 1
	else:
		return pascal (row - 1, col - 1) + pascal (row - 1, col)

# driver code
num = int (input ("Enter a nonnegative integer: "))
print ("Row {:d}: ".format (num), end ='')
for i in range (num + 1):
	print (pascal (num, i), end = ' ')
print ()
	
