def sum_up (x) :
	sum_n = 0
	for char in str (x):
		sum_n += int (char)
	return sum_n







# sum up
sum_n = 0
for i in range (1000000):
	sum_n += sum_up (i+1)


print ("The sum of the digits in the number from 1 to one million is {:,d}.".format (sum_n))

