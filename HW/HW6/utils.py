import os
from shutil import copyfile

class recover:
	def ABC ():
		target_bk = "ABC.bk"
		target_file = "ABC.txt"
		# Remove if exist
		try:
		    os.remove(target_file)
		except OSError:
			    pass

		# Recover it from 'Greetings.bk'
		copyfile (target_bk, target_file)

