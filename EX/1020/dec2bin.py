def dec2bin_integer (num):
	if num > 1 :
		dec2bin_integer (int (num / 2))
	print (num % 2, end='')

def dec2bin_float (floating):
	counter = 1
	while counter <= 15 :
		if floating >= 0.5 ** counter:
			floating -= 0.5 ** counter
			print (1, end='')
		else:
			print (0, end='')
		counter += 1

number = float (input ("Enter a number to run dec2bin: "))
if number < 0:
	number = -number
	print ("-")
dec2bin_integer (int (number))
print ('.', end='')
dec2bin_float (number - int (number))
print ()


# 4 	3 	2 	1 	0 	-1 	-2 ...
# 16 	8	4	2	1	1/2	1/4 ...
