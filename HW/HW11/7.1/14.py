class Point:
	def __init__ (self):
		self.x = eval (input ("Please input a x coordinate: "))
		self.y = eval (input ("Please input a y coordinate: "))

	def distance (self, pt):
		return ((self.x - pt.x) ** 2 + (self.y - pt.y) ** 2) ** 0.5




# driver code

## input
X1 = Point ()
X2 = Point ()
print ("The distance between 2 input points is", X1.distance (X2))

