num1 = input ("Enter the first number:")
num2 = input ("Enter the second number:")

if num1.isdigit () and num2.isdigit () :
	print ("The sum is ", str (eval (num1) + eval (num2)) )
elif not num1.isdigit () :
	if not num2.isdigit () :
		print ("Neither entry was a proper number.")
	else :
		print ("The first entry was not a proper number")
else :
	print ("The second netry was not a proper number")
