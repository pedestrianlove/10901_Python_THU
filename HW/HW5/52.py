from utils import underline

# function area
def compute (first, second, third):
	avg = (first + second + third) / 3
	the_range = first - third
	return int (avg), the_range




# driver code


## input
grade_list = []
for i in range (5):
	grade = eval (input ("Enter grade " + str(i+1) + ": " + underline.start))
	print (underline.end, end='')
	grade_list.append (grade)

## process
grade_list.sort (reverse = True)
avg, the_range = compute (grade_list[0], grade_list[1], grade_list[2])

## output
print ("Range:", the_range)
print ("Average:", avg)

