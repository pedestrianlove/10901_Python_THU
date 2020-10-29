### Output Result
#Enter a quotation: You miss 100% of the shots you never take. -- Wayne Gretsky
#MENU
# 1. Count number of vowels in the quotation.
# 2. Count number of uppercase letters in the quotation.
#Select 1 or 2 from menu: 1
#Number of vowels: 15
#Enter a quotation: You miss 100% of the shots you never take. -- Wayne Gretsky
#MENU
# 1. Count number of vowels in the quotation.
# 2. Count number of uppercase letters in the quotation.
#Select 1 or 2 from menu: 2
#Number of uppercase letters 3

### Function area.
def main() :
	## Analyze a quotation.
	quotation = input ("Enter a quotation: ")
	
	## Show menu.
	print ("\nMENU")
	print (" 1. Count number of vowels in the quotation.")
	print (" 2. Count number of uppercase letters in the quotation.")
	
	## Input choice.
	choice = int (input ("Select 1 or 2 from menu: "))
	if choice == 1:
		print ("Number of vowels:", calculateNumberOfVowels (quotation))
	else:
		print ("Number of uppercase letters",
			calculateNumberOfCaps (quotation))

def calculateNumberOfVowels (quotation):
	numberOfVowels = 0
	for char in quotation:
		if char.upper () in "AEIOU":
			numberOfVowels += 1
	return numberOfVowels

def calculateNumberOfCaps (quotation):
	numberOfCaps = 0
	for char in quotation:
		if 'A' <= char <= 'Z':
			numberOfCaps += 1
	return numberOfCaps


### Flow control.
main ()	

