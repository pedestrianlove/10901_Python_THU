import math

# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'

# input
miles = eval (input ("Enter number of miles: " + underline.start))
print (underline.end, end = '')
yards = eval (input ("Enter number of yards: " + underline.start))
print (underline.end, end = '')
feet = eval (input ("Enter number of feet: " + underline.start))
print (underline.end, end = '')
inches = eval (input ("Enter number of inches: " + underline.start))
print (underline.end, end = '')

# process
total_inches = 63360 * miles + 36 * yards + 12 * feet + inches
total_meters = total_inches / 39.37
kilometers = int (total_meters / 1000)
meters = total_meters - 1000 * kilometers
centimeters = (meters - int (meters)) * 100
meters = int (meters)


# output
print ("Metric length:")
print ("  ", f'{kilometers:}', "kilometers")
print ("  ", f'{meters:}', "meters")
print ("  ", f'{centimeters:.1f}', "centimeters")
