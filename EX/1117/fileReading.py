def main ():
	filePath = "FirstPresidents.txt"
	display (filePath)
	print ()
	display_list (filePath)

def display (filePath):
	infile = open (filePath, 'r')
	for line in infile:
		print (line, end = '')
	infile.close ()

def display_list (filePath):
	infile = open (filePath, 'r')
	presidentList = []
	for line in infile:
		presidentList.append (line.rstrip ())
	print (presidentList)
	infile.close ()

# driver code
main ()
