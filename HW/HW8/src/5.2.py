import os

# 8
print ("5.2 - 8.")
## INPUT
fileName = os.path.join ("..", "data", "DOW.txt")
infile = open (fileName, 'r')
DOW = [line.strip ().split (',') for line in infile]
## PROCESS
DOW.sort (key = lambda x: (eval (x[5]) - eval (x[4]))/ eval (x[4]))
## OUTPUT
print ("Best performing stock: ", DOW[-1][0], (eval(DOW[-1][5]) - eval (DOW[-1][4])) / eval (DOW[-1][4]) * 100, '%')
print ("Worst performing stock: ", DOW[0][0], (eval(DOW[0][5]) - eval (DOW[0][4])) / eval (DOW[0][4]) * 100, '%')
print ()
print ()

# 10
print ("5.2 - 10.")
print ()
print ()



# 12
print ("5.2 - 12.")
## INPUT
fileName = os.path.join ("..", "data", "Justices.txt")
infile = open (fileName, 'r')
Justices = [justice.rstrip ().split (',') for justice in iter (infile) if eval (justice.split (',')[5]) == 0]
infile.close ()
## PROCESS
Justices.sort (key = lambda x:x[4])
## OUTPUT
print ("Current Justices:")
print ('\n'.join ([justice[0] + ' ' + justice[1] for justice in Justices]))
print ()
print ()



# 14
print ("5.2 - 14.")
## Function
def YrsServed (justice):
	yrs = eval (justice[5]) - eval (justice[4])
	if yrs < 0:
		yrs += 2015
	return yrs
## INPUT
state = input ("Enter a state abbreviation: ")
fileName = os.path.join ("..", "data", "Justices.txt")
infile = open (fileName, 'r')
Justices = [justice.split (',') for justice in iter (infile) if justice.split (',')[3] == state]
infile.close ()
## OUTPUT
print ("Justice".ljust (20), "Appointing Pres".ljust (18), "Yrs Served".ljust (18))
for justice in Justices:
	print (' '.join (justice[0:2]).ljust (20), end = '')
	print (justice[2].split ()[-1].ljust (20), end = '')
	print (str (YrsServed (justice)).ljust (20))
print ()
print ()



# 16
print ("5.2 - 16.")
## INPUT
fileName = os.path.join ("..", "data", "Pioneers.txt")
infile = open (fileName, 'r')
Pioneers = {man.strip ().split (',')[0]:man.strip ().split (',') for man in iter (infile)}
infile.close ()
for man in Pioneers:
	print (man, end = '\t')
print ()
name = input ("Enter the name of a computer pioneer: ")
## OUTPUT
print (' '.join (Pioneers[name]) + '.')
print ()
print ()



# 18
print ("5.2 - 18.")
## INPUT
state = input ("Enter a state abbreviation: ")
fileName = os.path.join ("..", "data", "Colleges.txt")
infile = open (fileName, 'r')
University = [U.split(',') for U in iter (infile) if U.split(',')[1] == state]
## PROCESS && OUTPUT
University.sort (key = lambda x: eval (x[2]), reverse = True)
print ("Last college in " + state + " founded before 1800:" )
print (University[0][0])
print ()
print ()



# 20
print ("5.2 - 20.")
## INPUT
state = input ("Enter the name of a state: ")
fileName = os.path.join ("..", "data", "StatesANC.txt")
infile = open (fileName, 'r')
STATES = [states.split (',') for states in iter (infile) if states.split (',')[0] == state]
print ("Abbreviation: " + STATES[0][1])
print ("Nickname: " + STATES[0][2])
print ("Capital: " + STATES[0][3])
print ()
print ()




# 22
print ("5.2 - 22.")
## INPUT
target = eval (input ("Enter year from 1928-2013: "))
fileName = os.path.join ("..", "data", "Oscars.txt")
infile = open (fileName, 'r')
## OUTPUT
yr = 1927
for line in iter (infile):
	yr += 1
	if (yr == target):
		print ("Best Film: " + line.split (',')[0])
		print ("Genre: " + line.split (',')[1])
		break;
print ()
print ()




#24
print ("5.2 - 24.")
## INPUT
inFileName = os.path.join ("..", "data", "Cowboy.txt")
infile = open (inFileName, 'r')
equipment = [line.rstrip ().split (',') for line in iter (infile)]
infile.close ()
## PROCESS
for item in equipment:
	if item[0] == 'Saddle':
		item[1] = str (eval (item[1]) * .8)
		break
## OUTPUT
outFileName = os.path.join ("..", "data", "Cowboy2.txt")
outfile = open (outFileName, 'w')
for eq in equipment:
	outfile.write (','.join (eq) + '\n')
outfile.close ()
print ("Output saved to '" + outFileName + "'.")
print ()
print ()




# 26
print ("5.2 - 26.")
outFileName = os.path.join ("..", "data", "Cowboy.txt")
outfile = open (outFileName, 'a')
outfile.write ('Winchester Rifle,20.50\n')
outfile.close ()
print ("Output saved to '" + outFileName + "'.")
print ()
print ()
