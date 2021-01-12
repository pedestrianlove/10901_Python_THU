def verbalizeNumber (number):
	num_list = [[" "], ["thousand"], ["million"], ["billion"], ["trillion"], ["quadrillion"], ["quintillion"], ["sextillion"], ["septillion"]]
	for num_pos in num_list:
		num_pos.append (number % 1000)
		number = number // 1000

	num_list.reverse ()
	for num_pos in num_list:
		print ("{:3d}".format (num_pos[1]), num_pos[0])


# driver code
num = eval (input ("Input a number: "))
verbalizeNumber (num)
	
