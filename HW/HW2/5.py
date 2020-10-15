import math

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
SPY = eval (input ("Enter amount invested in SPY: " + underline.start))
print (underline.end, end = '')
QQQ = eval (input ("Enter amount invested in QQQ: " + underline.start))
print (underline.end, end = '')
EEM = eval (input ("Enter amount invested in EEM: " + underline.start))
print (underline.end, end = '')
VXX = eval (input ("Enter amount invested in VXX: " + underline.start))
print (underline.end, end = '')


# output
TRUE_SUM = SPY + QQQ + EEM + VXX
SUM = (float) (TRUE_SUM / 100)
print ("\nETF\t  PERCENTAGE")
print ("--------------------")
print ("SPY\t", f'{SPY/SUM:9.2f}%')
print ("QQQ\t", f'{QQQ/SUM:9.2f}%' )
print ("EEM\t", f'{EEM/SUM:9.2f}%')
print ("VXX\t", f'{VXX/SUM:9.2f}%')
print ("\nTOTAL AMOUNT INVESTED: ", f'${TRUE_SUM:,.2f}')
