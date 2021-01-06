class Fraction:
	def __init__ (self):
		self._numerator = eval (input ("Enter numerator of fraction: "))
		self._denominator = eval (input ("Enter denominator of fraction: "))

	def reduction (self):
		gcd = self.__gcd (self._numerator, self._denominator)
		self._numerator /= gcd
		self._denominator /= gcd


	def __gcd (self, x, y):
		if x < y:
			return self.__gcd (y, x)
		if x == 0 or y == 0:
			return x + y
		return self.__gcd (y, x % y)
		
	def __str__ (self):
		self.reduction ()
		return "{:d}/{:d}".format (int (self._numerator), int (self._denominator))
		
