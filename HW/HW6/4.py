# init list
list1 = ["Hello", "Aloha\n"]

# Write file
outfile = open ("Greetings.txt", 'a')
outfile.writelines (list1)
outfile.close ()

# Read from file
infile = open ("Greetings.txt", 'r')
text = infile.read ().rstrip ()
infile.close ()

# Output
print (text)	

#### OUTPUT LOG ####	
# (If ran after 2.py)
#Hello
#Aloha
#HelloAloha
# (If ran first)
#HelloAloha
