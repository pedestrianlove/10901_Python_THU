class Nation:
	def __init__ (self, nation):
		self._nation = nation[0]
		self._continent = nation[1]
		self._population = eval (nation[2])
		self._area = eval (nation[3])
				
	def popDensity (self):
		return self._population / self._area
