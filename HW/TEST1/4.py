class ITEM:
	def __init__ (self):
		self.item_name = input ("Enter name of item purchased: ")
		self.purchased_year = eval (input ("Enter year purchased: "))
		self.item_cost = eval (input ("Enter cost of item: "))
		self.estimatedLife = eval (input ("Enter estimated life of item (in years): "))
		self.dep_method = input ("Enter method of depreciation (SL or DDB): ")
		if self.dep_method == "DDB":
			self.method = "double-declining balance"
		else:
			self.method = "straight-line"
	def output_data (self):
		print (" ")
		print ("Description: " + self.item_name)
		print ("Year of purchase: {:d}".format (self.purchased_year))
		print ("Cost: ${:,.2f}".format (self.item_cost))
		print ("Estimated life: {:d} years".format (self.estimatedLife))
		print ("Method of depreciation: " + self.method)

	def output_chart (self):
		print ("Value at".rjust (30, ' ') + "Amount Deprec".rjust (20, ' '), "Total Depreciation".rjust (20, ' '))
		print ("Beg of Yr".rjust (30, ' ') + "During Year".rjust (20, ' '), "to End of Year".rjust (20, ' '))
		current_value = self.item_cost
		dep_sum = 0
		for i in range (self.purchased_year, self.purchased_year + self.estimatedLife + 1):
			if self.estimatedLife == 0:
				break
			if self.dep_method == "DDB":
				rate = 2 * (1 / self.estimatedLife)
				dep = rate * current_value
			else:
				rate = (1 / self.estimatedLife)
				dep = rate * self.item_cost
			print (i, end='')
			print ("{:,.2f}".format(current_value).rjust (26, ' '), end='')
			print ("{:,.2f}".format(dep).rjust (20, ' '), end='')
			current_value -= dep
			self.estimatedLife -= 1
			dep_sum += dep
			print ("{:,.2f}".format(dep_sum).rjust (20, ' '))

# driver code
item = ITEM ()
item.output_data ()
item.output_chart ()

