import math
from decimal import *

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
face_value = eval (input ("Enter face value of bond: " + underline.start))
print (underline.end, end = '')
interest_rate = float (input ("Enter coupon interest rate : " + underline.start))
print (underline.end, end = '')
market_price = eval (input ("Enter current market price: " + underline.start))
print (underline.end, end = '')
years_to_mature = eval (input ("Enter years until maturity: " + underline.start))
print (underline.end, end = '')

# process
a = ( ( face_value - market_price ) / years_to_mature )
b = ( ( face_value + market_price ) / 2 )
approx_YTM = (float) ( (interest_rate * face_value + a) / b )

# output
print ("Approximate YTM: ", f"{approx_YTM*100:.2f}%")
