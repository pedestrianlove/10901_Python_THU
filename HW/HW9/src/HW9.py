# init utils
import random
from stateCapitalData import CapitalNState 
HW9 = CapitalNState ()


## 6.1
print ("-------------------Section 6.1----------------------")

### 30 (State Capitals)
print ("30 (State Capitals):")
stateCapitals = HW9.CapitalList

while (True):
	INPUT = input ("Enter a state capital to delete (enter space to quit): ")
	if (INPUT == ' '):
		print ("Bye!")
		break

	if (INPUT in HW9.CapitalList):
		if (INPUT in stateCapitals):
			stateCapitals.remove (INPUT)
			print ("Capital deleted.")
		else:
			print ("Capital already deleted.")
	else:
		print ("Not a state capital.")

print ()
print ()






## 6.2
print ("-------------------Section 6.2----------------------")

### 10 (Perfect Square)
print ("10 (Perfect Square):")
print (random.randint (1, 100) ** 2)
print ()
print ()



### 12 (Vowel)
print ("12 (Vowel):")
randTarget = 'aeiou'
print (random.sample (randTarget, 1)[0])
print ()
print ()



### 14 (Dice)
print ("14 (Dice):")
targetSum = 0
for i in range (100000):
	if random.randint (1, 6) + random.randint (1, 6) == 7:
		targetSum += 1
print ("The probability of appearance of sum of 7 is approximately {:.3f}%".format (targetSum / 1000))
print ()
print ()



### 16 (U.S. States)
print ("16 (U.S. States):")
statesList = HW9.StatesAlpha
randomList = random.sample (statesList, 50)
HW9.writeList (randomList, 'RandomStates.txt')
print ("The output was dumped into 'RandomStates.txt' successfully.")
print ()
print ()



### 18 (Rock, Paper, Scissors)
print ("18 (Rock, Paper, Scissors):")
RPS = ['rock', 'paper', 'scissors']
player1 = random.randint (0, 2)
print ("Player 1: " + RPS[player1])
player2 = random.randint (0, 2)
print ("Player 2: " + RPS[player2])
if (player1 + 1) % 3 == player2:
	print ("Player 2 wins.")
elif (player2 + 1) % 3 == player1:
	print ("Player 1 wins.")
else:
	print ("Tied.")
print ()
print ()



### 20 (Powerball Lottery)
print ("20 (Powerball Lottery):")
consec_count = 0
for i in range (100000):
	sample = random.sample (range (1, 60), 5)
	sample.sort ()
	for i in range (4):
		if sample[i] + 1 == sample[i+1]:
			consec_count += 1
			break
print ("{:.3f}% of the time there were at least two consecutive numbers in the set of five numbers.".format (consec_count / 1000))
print ()
print ()



### 22 (Locate First Ace)
print ("22 (Locate First Ace):")
count_sum = 0
for i in range (100000):
	sample = random.sample (range (52), 52)
	for i in range (52):
		if sample[i] % 13 == 0:
			count_sum += (i + 1)
			break;
print ("The average number of cards turned up was {:.3f}.".format (count_sum / 100000))
print ()
print ()



### 24 (State Capital Quiz)
print ("24 (State Capital Quiz):")
state2Capital = {elem[0]:elem[3] for elem in HW9.StatesANC}
sample = random.sample (HW9.StatesAlpha, 5)
WRONG = []
for i in range (5):
	ANS = input ("What is the capital of " + sample[i] + ": ")
	if (ANS != state2Capital[sample[i]]):
		WRONG.append (state2Capital[sample[i]] + " is the capital of " + sample[i] + ".")
print ("You missed {:d} question(s).".format (len (WRONG)))
for wrong in WRONG:
	print (wrong)
print ()
print ()
