import math

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
price = eval (input ("Enter price of item: " + underline.start))
print (underline.end, end = '')
print ("Enter weight of item in pounds and ounces separately.")
pounds = eval (input ("Enter pounds: " + underline.start))
print (underline.end, end = '')
ounces = eval (input ("Enter ounces: " + underline.start))
print (underline.end, end = '')


# output
print ("Price per ounce: ", "${:,.2f}".format (price / (pounds * 16 + ounces)))
