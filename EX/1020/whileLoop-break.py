# input premise
list1 = []
print ("(Enter -1 to terminate entering numbers.)")

while True:
	# input
	num = eval (input ("Enter a nonnegative number: "))
	if num == -1 :
		break
	list1.append (num)
