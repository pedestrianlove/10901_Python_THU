# Was
# outfile = open (ABC.txt, 'a')

# Should be (string quotes)
outfile = open ("ABC.txt", 'a')
outfile.write ("D\n")
outfile.close ()


# Recover ABC.txt
from utils import recover
recover.ABC ()


