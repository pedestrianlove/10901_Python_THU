# for formatting purpose
class underline :
	start = '\033[04m'
	end = '\033[0m'
# store person method
class rMonth :
	months = []
	r_months = []
	def __init__ (self):
		fp = open ("32.input", "r")
		for month in iter (fp):
			self.months.append (month.strip ())
		fp.close ()

	def purify (self):
		for month in self.months :
			if 'r' in month or 'R' in month:
				self.r_months.append (month)
	def display (self):
		print ("The R months are: ")
		print (", ".join (self.r_months))


# driver code
listing = rMonth ()
listing.purify ()
listing.display ()
	
	
	
