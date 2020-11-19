# Was
#outfile = open ("ABC.txt", 'r')

# Should be (wrong file flag)
outfile = open ("ABC.txt", 'w')
outfile.write ("D\n")
outfile.close ()


# Recover ABC.txt
from utils import recover
recover.ABC ()


