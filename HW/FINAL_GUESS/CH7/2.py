class SavingsAccount:
	def __init__ (self):
		self._name = input ("Enter person's name: ")
		print ("D = Deposit, W = Withdrawal, Q = Quit")
		self._balance = 0

	def makeDeposit (self, money):
		money = eval (input ("Enter amount to deposit: "))
		self._balance += money
		print (self)
	
	def makeWithdrawal (self): # no over withdrawal
		money = eval (input ("Enter amount to withdraw: "))
		if (money > self._balance):
			print ("Insufficient funds, transaction denied.")
		else:
			self._balance -= money
		print (self)
	
	def __str__ (self):
		return "Balance: ${:,.2f}".format (self._balance)


# driver code
account = SavingsAccount ()
while (True):
	control = input ()
