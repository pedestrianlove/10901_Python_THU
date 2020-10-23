# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# variables
simple_base = 1000.00
simple = 1000.00
compound = 1000.00
rate = 1.05

# process && output
print ("\tSimple Interest\t", end='')
print ("Compound Interest")
for i in range(4):
	print (str(i + 1) + "\t", end='')
	simple += simple_base * (rate-1)
	compound = compound * rate
	print ("${:,.2f}".format (simple), end='\t')
	print ("${:,.2f}".format (compound))


	
	
	
