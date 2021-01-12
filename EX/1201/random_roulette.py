import random

def main ():
	bankroll = int (input ("Enter the amount of bankroll: "))
	amount, timesPlayed = playDoubleOrNothing (bankroll)
	print ("Ending bankroll:", amount, "dollars")
	print ("Number of games played:", timesPlayed)

def isOdd (n):
	if (1 <= n <= 36) and (n % 2 == 1):
		return True
	else:
		return False

def profit (n):
	if isOdd (n):
		return 1
	else:
		return -1

def playDoubleOrNothing (bankroll):
	amount = bankroll
	timesPlayed = 0
	while 0 < amount < 2 * bankroll:
		n = random.randint (0, 37)
		timesPlayed += 1
		amount += profit (n)
	return amount, timesPlayed

# driver code
main ()
