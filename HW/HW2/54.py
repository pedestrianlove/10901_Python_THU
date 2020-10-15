# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
revenue = eval (input ("Enter revenue: " + underline.start)) 
print (underline.end, end = '')
expenses = eval (input ("Enter expenses: " + underline.start)) 
print (underline.end, end = '')

# output
print ("Net income: ", "${:,.2f}".format (revenue - expenses))


