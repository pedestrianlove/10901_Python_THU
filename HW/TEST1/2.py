# 2. Prime Factors

# function area
def extremePrime (n):
	num = 2
	num_list = []
	while (n > 1):
		if n % num == 0:
			num_list.append (num)
			n = n / num
		else:
			num += 1
	return max (num_list), min (num_list)


# driver code
num = eval (input ("Entre a positive integer > 1: "))
largest, smallest = extremePrime (num)
print ("Largest prime factor: {:d}".format (largest))
print ("Smallest prime factor: {:d}".format (smallest))
