# for formatting purpose
class underline :
	start = '\033[04m'
	end = '\033[0m'
# store person method
class rMonth :
	months = []
	def __init__ (self):
		fp = open ("32.input", "r")
		for month in iter (fp):
			self.months.append (month.strip ())
		fp.close ()

	def purify (self):
		for month in self.months :
			if not ('r' in month or 'R' in month):
				self.months.remove (month)
	def display (self):
		print ("The R months are: ")
		print (", ".join (self.months))


# driver code
listing = rMonth ()
listing.purify ()
listing.display ()
	
	
	
