# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
coeff = float ( input ("Enter coefficient of restitution: " + underline.start))
print (underline.end, end='')
height = float ( input ("Enter initial height in meters: " + underline.start))
print (underline.end, end='')

# process
bounces = 0
traveled = 0.0
while (height >= 0.1) :
	traveled += (height + coeff * height )
	height *= coeff
	bounces += 1
traveled -= height;

# output
print ("Number of bounces: ", end='')
print ("{:,d}".format (bounces))

print ("Meters traveled: ", end='')
print ("{:.2f}".format (traveled))

	
	
	
