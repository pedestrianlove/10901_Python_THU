class Register:
	def __init__ (self):
		self._carPassed = 0
		self._moneyCollected = 0

	def collect (self):
		kind = input ("Enter type of vehicle (car/truck): ")
		self._carPassed += 1
		print ("Number of vehicles: {:d}".format (self._carPassed))
		if (kind == "car"):
			self._moneyCollected += 1
		elif (kind == "truck"):
			self._moneyCollected += 2
		print (self)
	
	def check (self):
		ans = input ("Do you want to enter more vehicles (Y/N)? ")
		if ans == 'Y':
			return True
		else:
			return False

	def __str__ (self):
		return "Money Collected: ${:.2f}".format (self._moneyCollected)
			

# driver code
reg = Register ()

while True:
	reg.collect ()
	if not reg.check ():
		break
print ("Have a good day.")
