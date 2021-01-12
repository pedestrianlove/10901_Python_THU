from utils import underline

# function
def INPUT ():
	firstName = input ("Enter first name: " + underline.start)
	print (underline.end, end='')
	lastName = input ("Enter last name: " + underline.start)
	print (underline.end, end='')
	salary = float (input ("Enter current salary: " + underline.start) )
	print (underline.end, end='')
	return firstName, lastName, salary

def pay_raise (salary):
	if (salary <= 40000):
		new_salary = salary * 1.05
	else :
	 	new_salary = (salary - 40000) * 1.02 + 2000 + 40000
	return new_salary

def show_salary (firstName, lastName, salary):
	print ("New salary for " + firstName + " " + lastName + ": ${:,.2f}".format (salary))

# main flow
def main ():
	firstName, lastName, salary = INPUT ()
	salary = pay_raise (salary)
	show_salary (firstName, lastName, salary)


# driver code
main ()	
	
	
