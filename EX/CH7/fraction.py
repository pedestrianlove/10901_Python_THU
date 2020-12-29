class Fraction:
    def __init__(self):
        self._numerator = 0
        self._denominator = 1
       
    def setNumerator(self, numerator):
        self._numerator = numerator
    def getNumerator(self):
        return self._numerator

    def setDenominator(self, denominator):
        self._denominator = denominator
    def getDenominator(self):
        return self._denominator
    
    def GCD(self, m, n):   # Greatest Common Divisor
        while n != 0:
            t = n
            n = m % n
            m = t
        return m    

    def reduce(self):
        gcd = self.GCD(self._numerator, self._denominator)
        self._numerator = int(self._numerator / gcd)
        self._denominator = int(self._denominator / gcd)
     
