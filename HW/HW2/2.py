import math

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
loan = eval (input ("Enter amount of loan: " + underline.start))
print (underline.end, end = '')
rate = eval (input ("Enter interest rate (%): " + underline.start))
print (underline.end, end = '')
years = eval (input ("Enter number of years: " + underline.start))
print (underline.end, end = '')

# process
var_i = (float) (rate / 1200)
divident = var_i * loan
print ("divident: ", divident)
divider = 1 - (1 + var_i**(-12*years) )
print ("divider: ", divider)


# output
print ("Monthly payment: ", "${:,.2f}".format (divident / divider))
