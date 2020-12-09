import os

class CapitalNState:
	def __init__ (self):
		fileName = os.path.join ('..', 'data', 'StatesANC.txt')
		infile = open (fileName, 'r')
		self.StatesANC = [line.rstrip ().split (',') for line in iter (infile)]
		infile.close ()
		self.CapitalList = []
		for entry in self.StatesANC:
			self.CapitalList.append (entry[3])
		
		fileName = os.path.join ('..', 'data', 'StatesAlpha.txt')
		infile = open (fileName, 'r')
		self.StatesAlpha = [line.rstrip () for line in iter (infile)]
		infile.close ()

	def writeList (self, arr, fileName):
		fileName = os.path.join ('..', 'output', fileName)
		outfile = open (fileName, 'w')
		for line in arr:
			outfile.write (line.rstrip () + '\n')
		outfile.close ()
