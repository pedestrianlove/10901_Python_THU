import math

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
change = eval (input ("Enter amount of change: " + underline.start))
print (underline.end, end = '')

# process
quarters = int (change / 25)
change = change % 25

dimes = int (change / 10)
change = change % 10

nickels = int (change / 5)
change = change % 5

cents = change


# output
print ("Quarters: ", quarters, "\tDimes: ", dimes)
print ("Nickels: ", nickels, "\tCents: ", cents)
