def count_occur (string, substr):
	counter = 0
	for i in range (0, len (string)-1):
		if (string[ i : i+len (substr) ] == substr):
			counter += 1
	return counter

## input
some_str = input ("Input some string: ")
some_substr = input ("Input some substring: ")

print ("The occurence of " + some_substr + " is ", count_occur (some_str, some_substr))
