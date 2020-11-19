list1 = ["spam", "and", "eggs"]
outfile = open ("Data.txt", 'w')

for word in list1:
	outfile.write (word + "\n")
	# Was (Invalid parentheses and wrong type!)
	#outfile.write ((len (word))
	# Should be
	outfile.write (str (len (word)))

outfile.close ()
