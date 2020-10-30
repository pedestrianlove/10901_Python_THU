def count_occur (string, substr):
	counter = 0
	i = 0
	while (i < len (string)):
		if (string[ i : i+len (substr) ] == substr):
			counter += 1
			i += len (substr) 
		else :
			i += 1
	return counter

## input
some_str = input ("Input some string: ")
some_substr = input ("Input some substring: ")

print ("The occurence of " + some_substr + " is ", count_occur (some_str, some_substr))
