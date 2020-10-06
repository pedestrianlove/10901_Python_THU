num = [2020, 9, 29, 11, 30, 58]
print ("num list: ", num)

print ("the length of list num: ", len (num))
print ("the maximum value of list num: ", max (num))
print ("the minimum value of list num: ", min (num))
print ("the summation value of the list num: ", sum (num))
print ("the count of number 29: ", num.count (29))
print ("the first index of number 29: ", num.index (29))

num.reverse ()
print ("the reversed number list", num)
num.append (9487)
print ("append 9487 to num list: ", num)
num.extend ([94, 87])
print ("extend [94, 87] to num list: ", num)

num.remove (9)
print ("remove 9 from num list: ", num)
num.insert (2, 484)
print ("insert 2, 484 to num list: ", num)

print ("new num list: ", num + [0] * 3)

num.clear ()
print ("cleared num list: ", num)

del num
print ("list num is now deleted.")
