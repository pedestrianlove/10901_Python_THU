from _utils import outputFile as of
import os
# Preprocessing
of.clean ()
print ("Note that all output to file is dumped in 'OUTPUT.txt' with append mode for convenience.")
print ()


# 24
print ("24.")
print ("It will do nothing and print 'File already exists.'")
print ()




# 26
def findItemsInBoth (list1, list2):
	return list (set (list1).intersection (set (list2)))

## driver code for 26
print ("26.")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
print ("Given 2 different list:")
print ("list1 = ", list1)
print ("list2 = ", list2)
print ("The intersection of 2 list above will be: ", findItemsInBoth (list1, list2))
print ()




# 28
def fetchLastName (list1):
	return set ([fullname.split ()[-1] for fullname in list1])

## driver code for 28
print ("28.")
names = ["Donald Shell", "Harlan Mills", "Donald Knuth", "Alan Kay"]
print ("Given the list: ", names)
print ("We can construct a set of distinct last name:", fetchLastName (names))
print ()




# 34
def sizeOfNum (fileName):
	numFile = open (fileName, 'r')
	num_set = set ()
	counter = 0
	for line in iter (numFile):
		counter += 1
		num_set.add (eval (line))
	numFile.close ()
	# return distinct and non-distinct
	return len (num_set), counter

## driver code for 34
print ("34.")
fileName = os.path.join ("bin", "Numbers.txt")
distinct_size, full_size = sizeOfNum (fileName)
print ("The '" + fileName + "' has {0:d} numbers in total, with {1:d} distinct.".format (full_size, distinct_size))
print ()




# 36
def minNum (fileName):
	numFile = open (fileName, 'r')
	numSet = set ()
	for line in iter (numFile):
		numSet.add (eval (line))
	numFile.close ()
	return min (numSet)

## driver code for 36
print ("36.")
fileName = os.path.join ("bin", "Numbers.txt")
print ("The smallest number in '" + fileName + "' is {:d}.".format (minNum (fileName)))
print ()




# 38
def avg (fileName):
	numFile = open (fileName, 'r')
	summation = 0
	counter = 0
	for line in iter (numFile):
		counter += 1
		summation += eval (line)
	numFile.close ()
	# return distinct and non-distinct
	return summation / counter

## driver code for 38
print ("38.")
fileName = os.path.join ("bin", "Numbers.txt")
print ("The average of the numbers in '" + fileName + "' is {:,.1f}.".format (avg (fileName)))
print ()




# 40
def NoRMonth (fileName):
	monthFile = open (fileName, 'r')
	month_set = set ()
	print ("Given the file '" + fileName + "', we can construct the following set:")
	for line in iter (monthFile):
		month_set.add (line.strip ())
	print (month_set)	
	monthFile.close ()
	print ("After removing all month without character 'r', we have the following set:")
	Rmonth = set ()
	for month in month_set:
		if 'r' in month:
			Rmonth.add (month)
	print (Rmonth)
	of.write (40, Rmonth)
	
## driver code for 40
print ("40.")
fileName = os.path.join ("bin", "SomeMonths.txt")
NoRMonth (fileName)
print ()




# 42
def NoVowelName (fileName):
	nameFile = open (fileName, 'r')
	name_set = set ()
	print ("Given the file '" + fileName + "', we can construct the following set:")
	for line in iter (nameFile):
		name_set.add (line.strip ())
	print (name_set)	
	nameFile.close ()
	print ("After removing all names that does not start from vowels, we have the following set:")
	vowelName = set ()
	for name in name_set:
		if name[0].lower () in 'aeiou':
			vowelName.add (name)
	print (vowelName)
	of.write (42, vowelName)
	
## driver code for 42
print ("42.")
fileName = os.path.join ("bin", "SomePlayers.txt")
NoVowelName (fileName)
print ()




# 44
def presidentState (fileName):
	stateFile = open (fileName, 'r')
	state_set = set ()
	print ("Given the file '" + fileName + "', we can construct the following set:")
	for line in iter (stateFile):
		state_set.add (line.strip ())
	print (state_set)
	stateFile.close ()
	print ("Hence, we can know that there are {:d} different states which produced presidents of the United States.".format (len (state_set)))
	of.write (44, state_set)

## driver code for 44
print ("44.")
fileName = os.path.join ("bin", "PresStates.txt")
presidentState (fileName)
print ()




# 46
def nameInsert (fileName):
	nameFile = open (fileName, 'r')
	name_set = set ()
	print ("Given the file '" + fileName + "', we can construct the following set:")
	for line in iter (nameFile):
		name_set.add (line.strip ())
	print (sorted (name_set), "\nTotal length: ", len (name_set))
	nameFile.close ()
	nameString = input ("Choose a name to insert: ")
	name_set.add (nameString)
	print ("The set is now:")
	name_set_sorted = sorted (name_set)
	print (name_set_sorted, "\nTotal length: ", len (name_set_sorted))
	return name_set_sorted

## driver code for 46
print ("46.")
fileName = os.path.join ("bin", "Names.txt")
of.write (46, nameInsert (fileName))
print ()


print ()
print ()
print ("All changes make to the file (if any) are dumped into 'OUTPUT.txt'.")
