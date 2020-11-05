# list to store country
countries = []

# read file
fp = open ("Country.txt", 'r')
for line in iter (fp):
	countries.append (line)
fp.close ()


# sort country
countries.sort ()


# output country
for i in range (6):
	print (countries[i])
