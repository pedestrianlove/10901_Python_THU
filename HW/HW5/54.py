# key function
def planet_names (elem):
	return elem[1]

	
	
# list
planets = [("Mercury", 75, 1), ("Venus", 460, 2), ("Mars", 140, 4), ("Earth", 510, 3), ("Jupiter", 62000, 5), ("Neptune", 7640, 8), ("Saturn", 42700, 6), ("Uranus", 8100, 7)]

# sort
planets.sort (key = planet_names, reverse = True)


# print
for elem in planets:
	print (elem[0] + " ", end='')
print ()

