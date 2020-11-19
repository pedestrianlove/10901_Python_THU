list1 = ["spam\n", "eggs\n"]
outfile = open ("Data.txt", 'w')
outfile.writelines (list1)
# print (len (outfile)) 
# outfile is a file object, which has no len () 
outfile.close ()
