import os

class outputFile:
	def clean ():
		if os.path.exists ("OUTPUT.txt"):
			os.remove ("OUTPUT.txt")
	def write (num, sth, fileName):
		outFile = open (fileName, 'w')
		#outFile.write (str(num) + '.\n')
		for elem in sth:
			outFile.write (elem + '\n')
		outFile.write ('\n\n')
		outFile.close ()

