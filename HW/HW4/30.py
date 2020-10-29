# for formatting purpose
class underline :
	start = '\033[04m'
	end = '\033[0m'
# store person method
class person :
	def __init__ (self):
		self.firstName = input ("Enter first name: " + underline.start)
		print (underline.end, end='')
		self.lastName = input ("Enter last name: " + underline.start)
		print (underline.end, end='')
		self.salary = float (input ("Enter current salary: " + underline.start) )
		print (underline.end, end='')

	def pay_raise (self):
		if (self.salary <= 40000):
			new_salary = self.salary * 1.05
		else :
		 	new_salary = (self.salary - 40000) * 1.02 + 2000 + 40000
		
		self.salary = new_salary

	def show_salary (self):
		print ("New salary for " + self.firstName + " " + self.lastName + ": ${:,.2f}".format (self.salary))


# driver code
human = person ()
human.pay_raise ()
human.show_salary ()
	
	
	
