# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
future = eval (input ("Enter future value: " + underline.start))
print (underline.end, end = '')
rate = eval (input ("Enter interest rate (as %): " + underline.start))
print (underline.end, end = '')
year = eval (input ("Enter number of years: " + underline.start))
print (underline.end, end = '')


# output
print ("Present value: ", "${:,.2f}".format (future / (1 + rate / 100)**year) )
