# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
hourly_wage = eval ( input ("Enter hourly wage: " + underline.start))
print (underline.end, end='')
working_hours = eval ( input ("Enter number of hours worked: " + underline.start))
print (underline.end, end='')


# output
print ("Gross pay for week is ", end='')
if (working_hours <= 40) :
	print ("${:.2f}.".format (working_hours * hourly_wage))
else :
	print ("${:.2f}.".format ((40 * hourly_wage) + (1.5 * (working_hours - 40) * hourly_wage)))

	
	
	
