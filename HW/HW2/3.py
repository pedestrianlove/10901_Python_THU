import math

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
face_value = eval (input ("Enter face value of bond: " + underline.start))
print (underline.end, end = '')
interest_rate = eval (input ("Enter coupon interest rate : " + underline.start))
print (underline.end, end = '')
market_price = eval (input ("Enter current market price: " + underline.start))
print (underline.end, end = '')
years_to_mature = eval (input ("Enter years until maturity: " + underline.start))
print (underline.end, end = '')

# process
a = (float) ( ( face_value - market_price ) / years_to_mature )
print (a)
b = (float) ( ( face_value + market_price ) / 2 )
print (b)
approx_YTM = (float) ( (interest_rate + a) / b )
print (approx_YTM)
# output
print ("Approximate YTM: ", f"{approx_YTM:.2f}%")
