# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


# input
grade = []
for i in range (5) :
	grade.append ( eval ( input ("Enter one of five grades: " + underline.start)) )
	print (underline.end, end='')

# process
grade.sort ()
avg = ( grade[2] + grade[3] + grade[4] ) / 3.0


# output
print ("Average grade: ", end='')
print ("{:.2f}".format (avg))

	
	
	
