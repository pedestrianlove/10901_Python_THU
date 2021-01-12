def main ():
	outfile = open ("FirstPresidents2.txt", 'w')
	createWithWritelines (outfile)
	outfile = open ("FirstPresidents3.txt", 'w')
	createWithWrite (outfile)

def createWithWritelines (outfile):
	presList = ["George Washington", "John Adams", "Thomas Jefferson"]
	outfile.writelines ([i + "\n" for i in presList])
	outfile.close ()

def createWithWrite (outfile):
	presList = ["George Washington", "John Adams", "Thomas Jefferson"]
	for elem in presList:
		outfile.write (elem + "\n")
	outfile.close ()

# driver code
main ()
