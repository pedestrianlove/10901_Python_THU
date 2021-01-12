# FIXME textbook required
# for formatting purpose
class underline:
    start = '\033[04m'
    end = '\033[0m'


## Bestow graduation honors.
# input
gpa = eval ( input ("Enter your gpa: " + underline.start))
print (underline.end, end='')

# Determine if honors are warranted.
if gpa >= 3.9:
	honors = " summa cum laude."
else:
	if gpa >= 3.6:
		honors = " magna cum laude."
	else :
		if gpa >= 3.3:
 			honors = " cum laude."
		else:
 			honors = "."
# Display conclusion.
print("You graduated" + honors)
	
	
	
