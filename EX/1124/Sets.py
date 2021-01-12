def main ():
	# Use a set to remove the duplicates from a list
	words = ["nudge", "nudge", "wink", "wink"]
	terms = set (words)
	print (terms)
	words = list (terms)
	print (words)

	# Add method
	print ("Adding \"nudge\"")
	terms.add ("nudge")
	print ("Adding \"maybe\"")
	terms.add ("maybe")
	print (terms)	

	# Discard method
	print ("Discarding \"nudge\"")
	terms.discard ("nudge")
	print (terms)

	# Set to tuple
	print ("Converting set to tuple...")
	words = tuple (terms)
	print (words)

# driver code
main ()
