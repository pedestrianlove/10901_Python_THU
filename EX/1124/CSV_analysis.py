def main ():
	## Do analysis of country's areas.
	areaAsStrings = extractField ("../CH5/UN.txt", 4)
	areas = [eval (num) for num in areaAsStrings]
	displaySomeStatistics (areas)

def extractField (fileName, n):
	## Extract the nth field from each record of a CSV file
	## and place the data into a list.
	infile = open (fileName, 'r')
	return [line.rstrip ().split (',')[n - 1] for line in infile]
	infile.close ()

def displaySomeStatistics (listOfNumbers):
	avg = sum (listOfNumbers) / len (listOfNumbers)
	median = calculateMedian (listOfNumbers)
	STD = calculateSTD (listOfNumbers, avg)
	print ("Average area: {0:,.2f} square miles".format (avg))
	print ("Median area: {0:,d} square miles".format (median))
	print ("Standard deviation: {0:,.2f} square miles".format (STD))

def calculateMedian (listOfNumbers):
	listOfNumbers.sort ()
	if len (listOfNumbers) % 2 == 1:
		median = listOfNumbers[int (len (listOfNumbers) / 2)]
	else:
		# median will be the avg of the 2 middle number
		m = int (len (listOfNumbers) / 2)
		median = (listOfNumbers[m] + listOfNumbers[m + 1]) / 2
	return median

def calculateSTD (listOfNumbers, avg):
	n = len (listOfNumbers)
	listOfSquaresOfDeviations = [0] * n
	for i in range (n):
		listOfSquaresOfDeviations[i] = (listOfNumbers[i] - avg) ** 2
	STD = (sum(listOfSquaresOfDeviations) / n) ** .5
	return STD

# driver code
main ()
