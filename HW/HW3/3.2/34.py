# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
balance = eval ( input ("Enter current balance: " + underline.start))
print (underline.end, end='')
withdrawal = eval ( input ("Enter amount of withdrawal: " + underline.start))
print (underline.end, end='')


# output
if (withdrawal > balance):
	print ("Withdrawal denied.")
else :
	balance -= withdrawal
	print ("The new balance is ", end='')
	print ("${:.2f}.".format (balance))
	if (balance < 150) :
		print ("(Balance below $150)")
	
	
	
