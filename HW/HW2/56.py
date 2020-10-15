# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
beginning = eval (input ("Enter beginning salary: " + underline.start))
print (underline.end, end = '')

# compute
new = beginning * 1.05 * 1.05 * 1.05

# output
print ("New salary: ", "${:,.2f}".format (new))
print ("Change: ", "{:.2f}%".format (( (new-beginning) / beginning) * 100))
