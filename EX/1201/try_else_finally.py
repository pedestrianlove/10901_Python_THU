import os

def main ():
	total = 0
	counter = 0
	foundFlag = True
	try:
		fileName = os.path.join ("..", "CH6", "Numbers.txt")
		infile = open (fileName, 'r')
	except FileNotFoundError:
		print ("File not found.")
		foundFlag = False
	if foundFlag:
		try:
			for line in infile:
				counter += 1
				total += float (line)
			print ("average:", total / counter)
		except ValueError:
			print ("Line", counter, "counld not be converted to a float.")
			if counter > 1:
				print ("Average so far:", total / (counter - 1))
				print ("Total so far:", total)
			else:
				print ("No average can be calculated.")
		except ZeroDivisionError:
			print ("File was empty.")
		else:
			print ("Total:", total)
		finally:
			infile.close ()
# driver code
main ()
