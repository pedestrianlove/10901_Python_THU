def main ():
	## Create a file containing all countries and areas, ordered by area.
	## Display first five lines of the file.
	countries = placeRecordsIntoList ("../CH5/UN.txt")
	countries.sort (key = lambda country : country[3], reverse = True)
	displayFiveLargestCountries (countries)
	writeNewFile (countries)

def placeRecordsIntoList (fileName):
	infile = open (fileName, 'r')
	listOfRecords = [line.rstrip () for line in iter (infile)]
	infile.close ()
	for i in range (len (listOfRecords)):
		listOfRecords[i] = listOfRecords[i].split (',')
		listOfRecords[i][2] = eval (listOfRecords[i][2])
		listOfRecords[i][3] = eval (listOfRecords[i][3])
	return listOfRecords

def displayFiveLargestCountries (countries):
	print ("{0:20}{1:9}".format ("Country", "Area (sq. mi.)"))
	for i in range (5):
		print ("{0:20}{1:9,d}".format (countries[i][0], countries[i][3]))

def writeNewFile (countries):
	outfile = open ("UNbyArea.txt", 'w')
	for country in countries:
		outfile.write (country[0] + ',' + str(country[3]) + '\n')

# driver code
main ()
