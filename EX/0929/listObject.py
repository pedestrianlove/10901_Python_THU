num = [2020, 9, 29, 11, 30, 58]
print ("num list: ", num)

print ("the length of list num: ", len (num))
print ("the maximum value of list num: ", max (num))
print ("the minimum value of list num: ", min (num))
print ("the summation value of the list num: ", sum (num))
print ("the count of number 29: ", num.count (29))
print ("the first index of number 29: ", num.index (29))

print ("the reversed number list", num.reverse ())
print ("append 9487 to num list: ", num.append (9487))
print ("extend [94, 87] to num list: ", num.extend ([94, 87]))


print ("remove 9 from num list: ", num.remove (9))
print ("insert 2, 484 to num list: ", num.insert (2, 484))

print ("new num list: ", num + [0] * 3)

print ("clear num list: ", num.clear ())

del num
print ("list num is now deleted.")
