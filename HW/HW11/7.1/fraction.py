import math
class Fraction:
	def __init__ (self, numerator = 0, denominator = -1):
		if (numerator == 0 and denominator == -1):
			self.numerator = eval (input ("Enter numerator of fraction: "))
			self.denominator = eval (input ("Enter denominator of fraction: "))
		else:
			self.numerator = numerator
			self.denominator = denominator

	# public
	def reduction (self):
		gcd = self.__gcd (self.numerator, self.denominator)
		#print (self.numerator, self.denominator, gcd)
		self.numerator /= gcd
		self.denominator /= gcd

	def sub (self, f2):
		tmp = Fraction (0, 0)
		tmp.numerator = self.numerator * f2.denominator - f2.numerator * self.denominator
		tmp.denominator = self.denominator * f2.denominator
		return tmp
	
	def add (self, f2):
		tmp = Fraction (0, 0)
		tmp.numerator = self.numerator * f2.denominator + f2.numerator * self.denominator
		tmp.denominator *= self.denominator * f2.denominator
		return tmp
	
	def mult (self, f2):
		tmp = Fraction (0, 0)
		tmp.numerator = self.numerator * f2.numerator
		tmp.denominator = self.denominator * f2.denominator
		return tmp

	def div (self, f2):
		tmp = Fraction (0, 0)
		tmp.numerator *= f2.denominator
		tmp.denominator *= f2.numerator
		return tmp 

	def sqrt (self):
		tmp = Fraction (self.numerator, self.denominator)
		tmp.numerator = math.sqrt (tmp.numerator)
		tmp.denominator = math.sqrt (tmp.denominator)
		return tmp

	# private
	def __gcd (self, x, y):
		if x < 0:
			x = -x
		if y < 0:
			y = -y
		if x < y:
			return self.__gcd (y, x)
		if x == 0 or y == 0:
			return x + y
		return self.__gcd (y, x % y)
		
	def __str__ (self):
		self.reduction ()
		return "({:d}/{:d})".format (int (self.numerator), int (self.denominator))
		
