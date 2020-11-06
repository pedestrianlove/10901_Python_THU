def main () :
	annual_roi, monthly_pay, beg_balance = input1 ()
	interest_paid, reduction, end_balance = compute (annual_roi, monthly_pay, beg_balance)
	output (interest_paid, reduction, end_balance)

def input1 () :
	annual_roi = eval (input ("Enter annual rate of interest: "))
	monthly_pay = eval (input ("Enter monthly payment: "))
	beg_balance = eval (input ("Enter beg. of month balance: "))
	return annual_roi, monthly_pay, beg_balance

def compute (annual_roi, monthly_pay, beg_balance):
	monthly_roi = (float)(annual_roi / 12)
	interest_paid = (0.01*monthly_roi) * beg_balance
	reduction = monthly_pay - interest_paid
	end_balance = beg_balance - reduction
	return interest_paid, reduction, end_balance




def output (interest_paid, reduction, end_balance):
	print ("Interest paid for the month: ${:,.2f}".format (interest_paid))
	print ("Reduction of principal: ${:,.2f}".format (reduction))
	print ("End of month balance: ${:,.2f}".format (end_balance))
	
main ()
