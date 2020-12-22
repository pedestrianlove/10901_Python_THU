import random

# init target num
num = random.randint (1, 100)
guess = 0
guess_count = 1
guess_int = 0

# start the first guessing
print ("I've thought of a number from 1 through 100.")
guess = input ("Guess the number: ").strip ()
if (not guess.isdigit ()):
	print ("You did not enter a number.")
elif (int (guess) not in range (1, 101)):
	print ("Number must be from 1 through 100.")
else:
	guess_int = int (guess)
	if (guess_int < num):
		print ("Too low")
	elif (guess_int > num):
		print ("Too high")
	else:
		print ("Correct. You took 1 guess.")
		
# continue guessing
while (guess_int != num):
	guess = input ("Try agian: ").strip ()
	guess_count += 1
	if (not guess.isdigit ()):
		print ("You did not enter a number.")
	elif (int (guess) not in range (1, 101)):
		print ("Number must be from 1 through 100.")
	else:
		guess_int = int (guess)
		if (guess_int < num):
			print ("Too low")
		elif (guess_int > num):
			print ("Too high")
		else:
			print ("Correct. You took {:d} guess.".format (guess_count))
