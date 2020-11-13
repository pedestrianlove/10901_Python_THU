# list to store country
countries = []

# read file
fp = open ("Countries.txt", 'r')
for line in iter (fp):
	countries.append (line)
fp.close ()


# sort country
countries.sort (key = len, reverse = True)


# output country
print ("\n".join (countries[:6]))
