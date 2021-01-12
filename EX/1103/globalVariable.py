# global
x = 0

# function area
def main ():
	print (str (x) + ": function main")
	trivial ()
	print (str (x) + ": function main")

def trivial ():
	global x
	x += 7
	print (str (x) + ": function trivial")

# driver code
main ()
