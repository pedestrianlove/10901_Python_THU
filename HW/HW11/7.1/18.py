from pairOfDice import PairOfDice


player = PairOfDice()
counter = 0
for i in range (10000):
	for j in range (24):
		player.roll ()
		if (player.sum () == 12):
			counter += 1
			break

print ("The rate for double-six is {:.4f}".format (counter / 10000))
