# Write data to file
outfile = open ("Greetings.txt", 'w')
outfile.write ("Hello\n")
outfile.write ("Aloha\n")
outfile.close ()

# Read data into the string 'text' from the file written
infile = open ("Greetings.txt", 'r')
text = infile.readline ().rstrip ()
infile.close ()


# output
print (text)

####OUTPUT LOG####
#Hello
