# input
list1 = []
print ("(Enter - 1 to terminate entering numbers.)")
num = eval (input ("Enter a nonnegative number: "))
while num != -1 :
	list1.append (num)
	num = eval (input ("Enter a nonnegative number: "))

# show result
length = len (list1)
if length > 0 :
	list1.sort ()
	print ("Minimum:", list1[0])
	print ("Maximum:", list1[-1])
	print ("Average:", sum (list1) / length)
else :
	print ("No nonnegative numbers were entered.")

