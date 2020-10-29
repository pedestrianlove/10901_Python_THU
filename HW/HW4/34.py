# for formatting purpose
class underline :
	start = '\033[04m'
	end = '\033[0m'
# store person method
class pension :
	def __init__ (self):
		self.age = eval (input ("Enter your age: " + underline.start))
		print (underline.end, end='')
		self.yrs = float (input ("Enter your month of service: " + underline.start)) / 12
		print (underline.end, end='')
		self.firstHigh = eval (input ("Enter your first of three highest salaries: " + underline.start))
		print (underline.end, end='')
		self.secondHigh = eval (input ("Enter your second of three highest salaries: " + underline.start))
		print (underline.end, end='')
		self.thirdHigh = eval (input ("Enter your third of three highest salaries: " + underline.start))
		print (underline.end, end='')
	
	def compute_avg (self):
		self.ave = ( self.firstHigh + self.secondHigh + self.thirdHigh ) / 3

	def compute_rate (self):
		if (self.yrs <= 5):
			perRate = 0.015 * self.yrs
		elif (self.yrs <= 10):
			perRate = 0.015 * 5 + 0.0175 * (self.yrs - 5)
		else :
			perRate = 0.015 * 5 + 0.0175 * 5 + (self.yrs - 10) * 0.02
		self.p = min (0.8, perRate)
	
	def isValid (self):
		if (self.age < 55 or self.yrs < 20):
			return False;
		return True;

	def display (self):
		print ("Annual pension: ", end='')
		print ("${:,.2f}".format (self.ave * self.p))
	


# driver code

retire = pension ()

if (not retire.isValid ()):
	print ("You are not qualified for any pension!")
else :
	retire.compute_avg ()
	retire.compute_rate ()
	retire.display ()
	
	
	
