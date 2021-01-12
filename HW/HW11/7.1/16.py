from pairOfDice import PairOfDice

# driver code
player1 = PairOfDice ()
player1.roll ()
player2 = PairOfDice ()
player2.roll ()

print ("Player 1:", player1.sum ())
print ("Player 2:", player2.sum ())


if (player1.sum () > player2.sum ()):
	print ("Player 1 wins.")
elif (player1.sum () < player2.sum ()):
	print ("Player 2 wins.")
elif (player1.sum () == player2.sum ()):
	print ("TIE")
else:
	print ("Something went wrong.")
