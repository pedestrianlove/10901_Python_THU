# key function
def length (elem):
	summation = 0
	for char in str (elem):
		summation += int (char)
	return summation

	
	
# list
numbers = [865, 1169, 1208, 1243, 329]

# sort
numbers.sort (key = length)


# print
print ("Sorted by sum of digits:")
print (numbers)
