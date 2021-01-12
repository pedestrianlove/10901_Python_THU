class Cab:
	def __init__ (self, typeof, mileage):
		self._type = typeof
		self._mileage = mileage
		
	def __str__ (self):
		return self._type + ": " + str (self._mileage) + " kilometers" 

class Sedan (Cab):
	def calculateFare (self):
		return 2 * self._mileage

class Hatchback (Cab):
	def calculateFare (self):
		return 1.5 * self._mileage



## driver code
cab_obj_list = []
while (True):
	typeof = input ("Enter cab type (Hatchback/Sedan): ")
	mileage = eval (input ("Enter the number of kilometers travelled: "))
	if (typeof == "Sedan"):
		cab_obj_list.append (Sedan (typeof, mileage))
	elif (typeof == "Hatchback"):
		cab_obj_list.append (Hatchback (typeof, mileage))
	
	ans = input ("Do you want to continue (Y/N)? ")
	if (ans == "N"):
		break

# output
print ("-----Kilometers driven for each cab-----")
mileage_sum = 0
fare_sum = 0
for cab in cab_obj_list:
	fare_sum += cab.calculateFare ()
	mileage_sum += cab._mileage
	print (cab)
print ("----------------------------------------")
print ()
print ("Total number of kilometers driven by all Cabs: {:.1f}".format (mileage_sum))
print ("Total fare earned from all cabs (in dollars): {:.1f}".format (fare_sum))
