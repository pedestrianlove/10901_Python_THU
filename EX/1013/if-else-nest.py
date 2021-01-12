color = input ("Enter a color (BLUE or RED): ")
mode = input ("Enter a mode (STEADY or FLASHING): ")

color = color.upper ()
mode = mode.upper ()

# process
result = ""
if color == "BLUE" :
	if mode == "STEADY" :
		result = "Clear View."
	else :
		result = "Clouds Due."
else :
	if mode == "STEADY" :
		result = "Rain Ahead."
	else :
		result = "Snow Ahead."

print (result)
