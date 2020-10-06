infile = open ("Data.txt", 'r')

listName = [line.rstrip () for line in infile]
# you can also replace "line.rstrip ()" with eval (line) if you want to evaluate int
print (", ".join (listName))

infile.close ()
