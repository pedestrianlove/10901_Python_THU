# input
num1 = eval (input ("Enter the first number: "))
num2 = eval (input ("Enter the second number: "))


# process
if num1 > num2 :
	print (str(num1) + ">" + str (num2))
elif num1 == num2 :
	print (str(num1) + "=" + str (num2))
else:
	print (str(num1) + "<" + str (num2))


# output
#print ("The larger value is", str (largerValue) + ".")
