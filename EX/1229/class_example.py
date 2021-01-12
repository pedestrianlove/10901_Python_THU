class Rectangle:
	def __init__ (self, width = 1, height = 1):
		self._width = width
		self._height = height

	def setWidth (self, width):
		self._width = width
	def setHeight (self, height):
		self._height = height


	def __str__ (self):
		print (self.width, self.height)
