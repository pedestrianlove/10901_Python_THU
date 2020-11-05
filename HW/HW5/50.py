from utils import underline

# function area
def semesterGrade (grade):
	if (100 >= grade >= 90):
		return 'A'
	elif (89 >= grade >= 80):
		return 'B'
	elif (79 >= grade >= 70):
		return 'C'
	elif (69 >= grade >= 60):
		return 'D'
	else:
		return 'F'


# driver code


## input
midterm = eval (input ("Enter grade on midterm: " + underline.start))
print (underline.end, end='')
final = eval (input ("Enter grade on final: " + underline.start))
print (underline.end, end='')

## process
grade = round ((float) ((midterm + final * 2) / 3 ))

## output
print ("Semester grade:", semesterGrade (grade))

