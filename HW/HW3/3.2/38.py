# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# premise
print ("The four railroad preperties are Reading, Pennsylvania, B & O, and Short Line.")

# input
selection = input ("Which is not a railroad?: " + underline.start)
print (underline.end, end='')


# output
if (selection == "Short Line") :
	print ("Correct.\nShort Line is a bus company.")
else :
	print ("Incorrect.\n" + selection + " is a railroad.")
	
	
