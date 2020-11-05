# key function
def length (elem):
	return str (elem)[-1]

	
	
# list
numbers = [865, 1169, 1208, 1243, 329]

# sort
numbers.sort (key = length, reverse = True)


# print
print ("Sorted by last digit:")
print (numbers)
