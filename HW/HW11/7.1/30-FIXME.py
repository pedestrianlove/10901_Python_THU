from fraction import Fraction
import math

class Polynomial:
	def __init__ (self):
		self.a = eval (input ("Please enter the value for 'a': "))
		self.b = eval (input ("Please enter the value for 'b': "))
		self.c = eval (input ("Please enter the value for 'c': "))

	def solvable (self):
		#tmp = Fraction (self.b.numerator, self.b.denominator)
		self.D = self.b * self.b - 4 * self.a * self.c
		if (self.D.numerator < 0):
			return False
		else:
			return True

	def solve (self):
		if (self.solvable ()):
			self.SOLVABLE = True
			self.sol = []
			SQRT = Fraction (math.sqrt (self.D), 2 * self.a)
			ANT = Fraction (-self.b, 2* self.a)
			self.sol.append (ANT.sub (SQRT))
			self.sol.append (ANT.add (SQRT))
		else:
			self.SOLVABLE = False
	
	
	def __str__ (self):
		output1 = "The polynomial" + str (self.a) + "x^2 + " + str (self.b) + "x + " + str (self.c) + " = 0 has the following solution(s) status: \n"
		if (self.SOLVABLE):
			output2 = str (self.sol[0]) + ", " + str (self.sol [1])
		else:
			output2 = "No real solutions."
		return output1 + output2

# driver code
poly = Polynomial ()
poly.solve ()
print (poly)
